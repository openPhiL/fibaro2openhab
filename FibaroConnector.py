import json
import requests 
import logging 
import time
import sys
from pprint import pformat

from configured_devices import *
from credentials import *

class FibaroConnector:
    logger = None
    session = None
    last_call_id = None

    def __init__(self):
        ## Log formatter:
        formatter = logging.Formatter( "%(asctime)s — %(name)s — %(levelname)s — %(message)s" )
        ## Logger Handler to console
        console_handler = logging.StreamHandler(sys.stdout)
        console_handler.setFormatter(formatter)
        console_handler.name = "consoleHandler"
        ## Logger Handler to file
        """
        file_handler = logging.handlers.RotatingFileHandler(self.log_file, maxBytes=5000, backupCount=1)
        file_handler.setFormatter(self.formatter)
        file_handler.name = "fileHandler"
        """
        #Load Logger
        self.logger = logging.getLogger('fibaro2openhab')
        self.logger.setLevel(logging.DEBUG)
        self.logger.addHandler(console_handler)
        ##//self.logger.addHandler(file_handler)
        #Load session
        fibaroLite_adapter = requests.adapters.HTTPAdapter(max_retries=3)
        self.session = requests.Session()
        self.session.mount(fibaro_url, fibaroLite_adapter)
        ##Load the initial last_call_id



    def pulling(self):
        while True:
            try:
                if not self.last_call_id:
                    self.logger.info("Startup: make extra call to retrieve last_call_id")
                    response_last_call_id = self.session.get(fibaro_url, auth=(fibaro_username, fibaro_password), timeout=31)
                    response_last_call_id_json = json.loads(response_last_call_id.text)
                    self.last_call_id = response_last_call_id_json['last']
                url = fibaro_url + '?last=' + str(self.last_call_id)
                self.logger.debug("calling url: " + url)  
                self.logger.debug('waiting on something to happen')
                response = self.session.get(url, auth=(fibaro_username, fibaro_password), timeout=31)
            except ( ConnectionError,  requests.Timeout) as error:
                self.logger.debug('failed to call: ' + url)
                self.logger.error('Error: ' + error)

            if response:
                try:
                    response_json = json.loads(response.text)
                    self.last_call_id = response_json['last']
                    return response_json
                except json.JSONDecodeError as error:
                    self.logger.error('JSON Decode error in ' + response.text)   
            else:
                self.logger.error('Response not received! will Wait 5 sec and try again')
            time.sleep(5)   
            continue      

    def post_to_openhab(self,openhabItem,new_data):
        post_url = url_openhab + openhabItem + '/state'
        self.logger.debug("URL:"+str(post_url))
        openhab_response = requests.put(url = post_url, data = new_data, verify=False, headers={"content-type":"text"}) 
        self.logger.debug('Response: ' +pformat(openhab_response))
        try:
            openhab_response_json = openhab_response.json()
            if openhab_response_json['error']:
                error = openhab_response_json['error']
                self.logger.error("Response: ("+str(error.get('http-code')) + ")" + error.get('message') )
        except ValueError:
            pass

    def watch(self):
        while True:
            triggeringID = None
            triggeringObject = None

            self.logger.debug('Wait for next Response ' + str(self.last_call_id)) 
            response_json = self.pulling( )
            if response_json['changes']:
                for current_change in response_json['changes']:

                    self.logger.debug('Response: ' + pformat(response_json))
                    self.logger.debug('Changes detected')
                    triggeringID = str(current_change['id'])
                    triggeringObject = configured_devices.get(triggeringID)
                    
                    if triggeringObject == None: 
                        self.logger.warning('Triggering Object with ID ' + triggeringID + ' is unknown or not mapped') 
                        continue
                    
                    for action in triggeringObject:                       
                        changed_data = current_change.get(action)
                        if changed_data:
                            mapped_value = triggeringObject[action].get(changed_data)
                            if mapped_value: 
                                self.logger.info(triggeringObject[action]['name'] + '('+ triggeringID +') triggered action was "' + action + '" with "' + changed_data +'" mapped to "' + mapped_value + '"')
                                self.post_to_openhab(triggeringObject[action]['name'], mapped_value)
                            else:
                                self.logger.info(triggeringObject[action]['name'] + '('+ triggeringID +') triggered action was "' + action + '" with "' + changed_data )
                                self.post_to_openhab(triggeringObject[action]['name'], changed_data)
                        else:
                            self.logger.debug(triggeringObject[action]['name'] + '('+ triggeringID +') defined action "' + action + '" was not found ')
                        