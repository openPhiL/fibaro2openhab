import logging
import json
from json.decoder import JSONDecodeError
import requests
from requests.adapters import HTTPAdapter
from requests.exceptions import RequestException
from requests.exceptions import ConnectionError
from requests.exceptions import Timeout
from requests.exceptions import HTTPError
import time

# create logger with 'spam_application'
logging.basicConfig(level=logging.DEBUG)
logger = logging.getLogger('fibaro2openhab')
logger.setLevel(logging.DEBUG)
# create file handler which logs even debug messages
# create console handler with a higher log level
ch = logging.StreamHandler()
ch.setLevel(logging.DEBUG)
# create formatter and add it to the handlers
formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
ch.setFormatter(formatter)
# add the handlers to the logger
logger.addHandler(ch)

 
logger.warning('Script is starting')

url = "http://172.16.10.11:80/api/refreshStates"
url_openhab = 'http://openhab2:8080/rest/items/' #openhbitem etc
logger.debug('setting http adapter to ' + url)
fibaroLite_adapter = HTTPAdapter(max_retries=3)
session = requests.Session()
session.mount(url, fibaroLite_adapter)


#get the last ID to be next in line with the fibaro script
while True:
    logger.debug('Retrieving last_id')
            
    try:
        last_response = session.get(url, auth=('admin', 'admin'), timeout=31)
        
        #get the last ID to be next in line with the fibaro script
        last_response_content = json.loads(last_response.text)
        last_call_id = last_response_content['last']
        logger.debug('Last ID received: ' + str(last_call_id))
        break
    except ( ConnectionError,  Timeout , JSONDecodeError ) as error:
        logger.error(error)
        logger.debug('Wait 5 sec')
        time.sleep(5)
        continue   


logger.warning('Script is initialized - starting the loop')

while True:
    logger.debug('Wait for next Response ' + str(last_call_id))

    try:
        #make a call with that ID to fetch next change
        current_request = url + '?last=' + str(last_call_id)
        current_response = session.get( current_request , auth=('admin', 'admin'), timeout=31)
    except ( ConnectionError, Timeout,  HTTPError ) as errh:
        logger.error(errh)
        logger.debug('Wait 5 sec')
        time.sleep(5)
        continue
   

    if current_response:
        logger.debug('Response received! (' + str(last_call_id) + ')')
        change_counter = 0
    else:
        logger.error('Response not received! ')
        logger.debug('Wait 5 sec')
        time.sleep(5)
        continue

    try:
        current_response_content = json.loads(current_response.text)
    except JSONDecodeError as je:
        logger.error(je)   
        logger.debug('Wait 5 sec')
        time.sleep(5)
        continue 



    last_call_id = current_response_content['last']
    if current_response_content['changes']:
        logger.debug('Changes detected')
        for current_change in current_response_content['changes']:
            triggeringID = str(current_change['id'])
            if triggeringID == '170':
                logger.critical(current_change)
            
            openhabItem = None 
            action = None
            #logger.debug(current_change)