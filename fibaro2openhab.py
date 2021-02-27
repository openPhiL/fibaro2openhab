#!/usr/bin/python3
import logging

from logging.handlers import RotatingFileHandler

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
logging.basicConfig(level=logging.INFO) 
logger = logging.getLogger('fibaro2openhab')
logger.setLevel(logging.INFO)
# create file handler which logs even debug messages
#fh = logging.FileHandler('/var/log/openhab2/fibaro2openhab.log')
fh = RotatingFileHandler('/var/log/openhab2/fibaro2openhab.log', mode='a', maxBytes=5*1024*1024, 
                                 backupCount=2, encoding=None, delay=0)

##fh = logging.FileHandler('fibaro2openhab.log')
fh.setLevel(logging.INFO)
# create console handler with a higher log level
#ch = logging.StreamHandler()
#ch.setLevel(logging.DEBUG)
# create formatter and add it to the handlers
formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
fh.setFormatter(formatter)
#ch.setFormatter(formatter)
# add the handlers to the logger
logger.addHandler(fh)
#logger.addHandler(ch)

 
logger.warning('Script is starting')

url = "http://172.16.10.11:80/api/refreshStates"
url_openhab = 'http://localhost:8080/rest/items/' #openhbitem etc
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
            openhabItem = None 
            action = None
            updateaction = 'post' #default
#Example:{'status': 'IDLE', 'last': 625011, 'date': '20:23 | 27.9.2019', 'timestamp': 1569615798, 'logs': [], 'events': [], 'changes': 
#[{'id': 11, 'log': '', 'logTemp': ''}, 
# {'id': 12, 'log': '', 'logTemp': ''}, 
# {'id': 13, 'log': '', 'logTemp': ''}, 
# {'id': 14, 'log': '', 'logTemp': ''}, 
# {'id': 15, 'log': '', 'logTemp': ''}], 
# 'alarmChanges': []}
            if 'log' in current_change :  
                logger.debug('change in log detected for ' + triggeringID +current_change['log'] )
                continue
            # PowerPlugs
            if 'power' in current_change :  
                logger.debug('change in power detected for ' + triggeringID )
#                if triggeringID == '54' :
#                    openhabItem = 'Kitchen_Outlet_Refrigerator_MeterWatts'
#                    action = current_change['power']
#                if triggeringID == '56' :
##                    openhabItem = 'Kitchen_Outlet_Freezer_MeterWatts'
#                    action = current_change['power']
#                if triggeringID == '113' :
#                    openhabItem = 'Kitchen_Outlet_Coffeemachine_MeterWatts'
#                    action = current_change['power']
#                if triggeringID == '175' :
#                    openhabItem = 'Livingroom_Outlet_Refrigerator_MeterWatts'
#                    action = current_change['power']

##            if 'energy' in current_change :  
##                logger.debug('change in power detected for ' + triggeringID )
##                if triggeringID == '54' :
##                    openhabItem = 'Kitchen_Outlet_Refrigerator_MeterKWh'
##                    action = current_change['energy']
##                if triggeringID == '56' :
##                    openhabItem = 'Kitchen_Outlet_Freezer_MeterKWh'
##                    action = current_change['energy']
##                if triggeringID == '113' :
##                    openhabItem = 'Kitchen_Outlet_Coffeemachine_MeterKWh'
##                    action = current_change['energy']
##                if triggeringID == '175' :
##                    openhabItem = 'Livingroom_Outlet_Refrigerator_MeterKWh'
##                    action = current_change['energy']

            # MotionSensors
            if 'value' in current_change :  
                if 'lastBreached' in current_change:
                    continue
                logger.debug('change in motion detected for ' + triggeringID )    

                #Livingroom
                if triggeringID == '191' :
                    openhabItem = 'WohnzimmerFensterVorneSensor_Position'
                    url_openhab = 'http://10.0.1.12:8080/rest/items/'
                    action = "OPEN" if str(current_change['value']) == 'true' else "CLOSED"
                    updateaction = 'put'
                if triggeringID == '192' :
                    openhabItem = 'WohnzimmerFensterVorneSensor_Temperatur'
                    url_openhab = 'http://10.0.1.12:8080/rest/items/'
                    action = current_change['value']
                    updateaction = 'put'
                    
                if triggeringID == '195' :
                    openhabItem = 'WohnzimmerFensterHintenSensor_Position'
                    url_openhab = 'http://10.0.1.12:8080/rest/items/'
                    action = "OPEN" if str(current_change['value']) == 'true' else "CLOSED"
                    updateaction = 'put'
                if triggeringID == '196' :
                    openhabItem = 'WohnzimmerFensterHintenSensor_Temperatur'
                    url_openhab = 'http://10.0.1.12:8080/rest/items/'
                    action = current_change['value']
                    updateaction = 'put'

                if triggeringID == '229' :
                    url_openhab = 'http://10.0.1.12:8080/rest/items/'
                    openhabItem = 'WohnzimmerFensterMitteSensor_Position'
                    updateaction = 'put'
                    action = "Gekippt" if str(current_change['value']) == 'true' else "Geschlossen"
                if triggeringID == '231' :
                    url_openhab = 'http://10.0.1.12:8080/rest/items/'
                    openhabItem = 'WohnzimmerFensterMitteSensor_Position'
                    updateaction = 'put'
                    action = "Offen" if str(current_change['value']) == 'true' else "Geschlossen"

                #UGFloor
                
                if triggeringID == '115' :
                    openhabItem = 'UntergeschossVorneBewegungsmelder_Bewegung'
                    url_openhab = 'http://10.0.1.12:8080/rest/items/'
                    #updateaction = 'put'
                    action = "ON" if str(current_change['value']) == 'true' else "OFF"
                if triggeringID == '116' :
                    url_openhab = 'http://10.0.1.12:8080/rest/items/'
                    openhabItem = 'UntergeschossVorneBewegungsmelder_Temperatur'
                    updateaction = 'put'
                    action = current_change['value']
                if triggeringID == '117' :
                    updateaction = 'put'
                    url_openhab = 'http://10.0.1.12:8080/rest/items/'
                    openhabItem = 'UntergeschossVorneBewegungsmelder_Helligkeit'
                    action = current_change['value']

                if triggeringID == '60' :
                    #updateaction = 'put'
                    url_openhab = 'http://10.0.1.12:8080/rest/items/'
                    openhabItem = 'UntergeschossHintenBewegungsmelder_Bewegung'
                    action = "ON" if str(current_change['value']) == 'true' else "OFF"
                if triggeringID == '61' :
                    updateaction = 'put'
                    url_openhab = 'http://10.0.1.12:8080/rest/items/'
                    openhabItem = 'UntergeschossHintenBewegungsmelder_Temperatur'
                    action = current_change['value']
                if triggeringID == '62' :
                    updateaction = 'put'
                    url_openhab = 'http://10.0.1.12:8080/rest/items/'
                    openhabItem = 'UntergeschossHintenBewegungsmelder_Helligkeit'
                    action = current_change['value']

                #WC
                if triggeringID == '5' :
                    updateaction = 'put'
                    url_openhab = 'http://10.0.1.12:8080/rest/items/'
                    openhabItem = 'WCBewegungsmelder_Bewegung'
                    action = "ON" if str(current_change['value']) == 'true' else "OFF"
                if triggeringID == '6' :
                    updateaction = 'put'
                    url_openhab = 'http://10.0.1.12:8080/rest/items/'
                    openhabItem = 'WCBewegungsmelder_Temperatur'
                    action = current_change['value']
                if triggeringID == '7' :
                    updateaction = 'put'
                    url_openhab = 'http://10.0.1.12:8080/rest/items/'
                    openhabItem = 'WCBewegungsmelder_Helligkeit'
                    action = current_change['value']

                #Kitchen

              

                #Dining
                # if triggeringID == '20' :
                #     openhabItem = 'Dining_SensorWindow_Motion'
                #     action = "ON" if str(current_change['value']) == 'true' else "OFF"
                # if triggeringID == '21' :
                #     openhabItem = 'Dining_SensorWindow_Temperature'
                #     action = current_change['value']
                # if triggeringID == '22' :
                #     openhabItem = 'Dining_SensorWindow_Luminance'
                #     action = current_change['value']

                if triggeringID == '137' :
                    updateaction = 'put'
                    url_openhab = 'http://10.0.1.12:8080/rest/items/'
                    openhabItem = 'EssbereichBewegungsmelder_Bewegung'
                    action = "ON" if str(current_change['value']) == 'true' else "OFF"
                if triggeringID == '138' :
                    updateaction = 'put'
                    url_openhab = 'http://10.0.1.12:8080/rest/items/'
                    openhabItem = 'EssbereichBewegungsmelder_Temperatur'
                    action = current_change['value']
                if triggeringID == '139' :
                    updateaction = 'put'
                    url_openhab = 'http://10.0.1.12:8080/rest/items/'
                    openhabItem = 'EssbereichBewegungsmelder_Helligkeit'
                    action = current_change['value']

                if triggeringID == '210' :
                    url_openhab = 'http://10.0.1.12:8080/rest/items/'
                    openhabItem = 'ErdgeschossFensterHintenTuereSensor_Position'
                    updateaction = 'put'
                    action = "Gekippt" if str(current_change['value']) == 'true' else "Geschlossen"
                if triggeringID == '212' :
                    url_openhab = 'http://10.0.1.12:8080/rest/items/'
                    openhabItem = 'ErdgeschossFensterHintenTuereSensor_Position'
                    updateaction = 'put'
                    action = "Offen" if str(current_change['value']) == 'true' else "Geschlossen"


                #Flur
                if triggeringID == '214' :
                    url_openhab = 'http://10.0.1.12:8080/rest/items/'
                    openhabItem = 'KucheBewegungsmelderHinten_Bewegung'
                    action = "ON" if str(current_change['value']) == 'true' else "OFF"
                if triggeringID == '215' :
                    url_openhab = 'http://10.0.1.12:8080/rest/items/'
                    openhabItem = 'KucheBewegungsmelderHinten_Temperatur'
                    action = current_change['value']
                if triggeringID == '216' :
                    url_openhab = 'http://10.0.1.12:8080/rest/items/'
                    openhabItem = 'KucheBewegungsmelderHinten_Helligkeit'
                    action = current_change['value']

                if triggeringID == '220' :
                    url_openhab = 'http://10.0.1.12:8080/rest/items/'
                    openhabItem = 'KucheBewegungsmelderVorne_Bewegung'
                    action = "ON" if str(current_change['value']) == 'true' else "OFF"
                if triggeringID == '221' :
                    url_openhab = 'http://10.0.1.12:8080/rest/items/'
                    openhabItem = 'KucheBewegungsmelderVorne_Temperatur'
                    action = current_change['value']
                if triggeringID == '222' :
                    url_openhab = 'http://10.0.1.12:8080/rest/items/'
                    openhabItem = 'KucheBewegungsmelderVorne_Helligkeit'
                    action = current_change['value']

                #Outside
                #if triggeringID == '233' :
                #    url_openhab = 'http://10.0.1.12:8080/rest/items/'
                #    openhabItem = 'KucheSensorVorne_Bewegung'
                #    action = "ON" if str(current_change['value']) == 'true' else "OFF"
                if triggeringID == '234' :
                    url_openhab = 'http://10.0.1.12:8080/rest/items/'
                    openhabItem = 'AussenSensor_Temperatur'
                    action = current_change['value']
                if triggeringID == '235' :
                    url_openhab = 'http://10.0.1.12:8080/rest/items/'
                    openhabItem = 'AussenSensor_Helligkeit'
                    action = current_change['value']

                #Bathroom
                if triggeringID == '131' :
                    updateaction = 'put'
                    url_openhab = 'http://10.0.1.12:8080/rest/items/'
                    openhabItem = 'BadezimmerBewegungsmelderWanne_Bewegung'
                    action = "ON" if str(current_change['value']) == 'true' else "OFF"
                if triggeringID == '132' :
                    updateaction = 'put'
                    url_openhab = 'http://10.0.1.12:8080/rest/items/'
                    openhabItem = 'BadezimmerBewegungsmelderWanne_Temperatur'
                    action = current_change['value']
                if triggeringID == '133' :
                    updateaction = 'put'
                    url_openhab = 'http://10.0.1.12:8080/rest/items/'
                    openhabItem = 'BadezimmerBewegungsmelderWanne_Helligkeit'
                    action = current_change['value']

                if triggeringID == '95' :
                    updateaction = 'put'
                    url_openhab = 'http://10.0.1.12:8080/rest/items/'
                    openhabItem = 'BadezimmerBewegungsmelderEingang_Bewegung'
                    action = "ON" if str(current_change['value']) == 'true' else "OFF"
                if triggeringID == '96' :
                    updateaction = 'put'
                    url_openhab = 'http://10.0.1.12:8080/rest/items/'
                    openhabItem = 'BadezimmerBewegungsmelderEingang_Temperatur'
                    action = current_change['value']
                if triggeringID == '97' :
                    updateaction = 'put'
                    url_openhab = 'http://10.0.1.12:8080/rest/items/'
                    openhabItem = 'BadezimmerBewegungsmelderEingang_Helligkeit'
                    action = current_change['value']

                #Masterbedroom
                if triggeringID == '11' :
                    url_openhab = 'http://10.0.1.12:8080/rest/items/'
                    openhabItem = 'SchlafzimmerEingangBewegungsmelder_Bewegung'
                    updateaction = 'put'
                    action = "ON" if str(current_change['value']) == 'true' else "OFF"
                if triggeringID == '12' :
                    url_openhab = 'http://10.0.1.12:8080/rest/items/'
                    openhabItem = 'SchlafzimmerEingangBewegungsmelder_Temperatur'
                    updateaction = 'put'
                    action = current_change['value']
                if triggeringID == '13' :
                    url_openhab = 'http://10.0.1.12:8080/rest/items/'
                    openhabItem = 'SchlafzimmerEingangBewegungsmelder_Helligkeit'
                    updateaction = 'put'
                    action = current_change['value']

                #LukasBedroom
                if triggeringID == '161' :
                    url_openhab = 'http://10.0.1.12:8080/rest/items/'
                    openhabItem = 'LukasZimmer_SensorUntermBett_Bewegung'
                    action = "ON" if str(current_change['value']) == 'true' else "OFF"
                if triggeringID == '162' :
                    url_openhab = 'http://10.0.1.12:8080/rest/items/'
                    openhabItem = 'LukasZimmer_SensorUntermBett_Temperatur'
                    action = current_change['value']
                if triggeringID == '163' :
                    url_openhab = 'http://10.0.1.12:8080/rest/items/'
                    openhabItem = 'LukasZimmer_SensorUntermBett_Helligkeit'
                    action = current_change['value']
                if triggeringID == '164' :
                    url_openhab = 'http://10.0.1.12:8080/rest/items/'
                    openhabItem = 'LukasZimmer_SensorUntermBett_Luftfeuchtigkeit'
                    action = current_change['value']

                #LeaBedroom
                if triggeringID == '167' :
                    url_openhab = 'http://localhost:8080/rest/items/' #openhbitem etc
                    openhabItem = 'Leabedroom_Sensor_Motion'
                    action = "ON" if str(current_change['value']) == 'true' else "OFF"
                if triggeringID == '168' :
                    url_openhab = 'http://localhost:8080/rest/items/' #openhbitem etc
                    openhabItem = 'Leabedroom_Sensor_Temperature'
                    action = current_change['value']
                if triggeringID == '169' :
                    url_openhab = 'http://localhost:8080/rest/items/' #openhbitem etc
                    openhabItem = 'Leabedroom_Sensor_Luminance'
                    action = current_change['value']

                # Salon
                if triggeringID == '178' :
                    url_openhab = 'http://10.0.1.12:8080/rest/items/'
                    openhabItem = 'SalonBewegungsmelder_Bewegung'
                    action = "ON" if str(current_change['value']) == 'true' else "OFF"
                if triggeringID == '179' :
                    url_openhab = 'http://10.0.1.12:8080/rest/items/'
                    openhabItem = 'SalonBewegungsmelder_Temperatur'
                    action = current_change['value']
                if triggeringID == '180' :
                    url_openhab = 'http://10.0.1.12:8080/rest/items/'
                    openhabItem = 'SalonBewegungsmelder_Helligkeit'
                    action = current_change['value']

                
            if openhabItem is not None and action is not None:
                logger.info('openhabItem: ' + openhabItem + ' set to ' + action  )
                post_url = url_openhab + openhabItem
                post_action = action
                logger.debug("URL:"+str(post_url))
                logger.debug("BODY:"+str(post_action))
                change_counter = change_counter + 1
                logger.debug("Change_counter: " + str(change_counter))
                try: 
                    if updateaction == 'post':
                        if url_openhab == 'http://localhost:8080/rest/items/':
                            post_request = requests.post(url = post_url, data = post_action, verify=False) 
                        else:
                            post_request = requests.post(url = post_url, data = post_action, verify=False, headers={"content-type":"text"}) 
                    else:
                        post_url = post_url + '/state'
                        post_request = requests.put(url = post_url, data = post_action, verify=False, headers={"content-type":"text"}) 
                        logger.info('URL:'+post_url)
                        logger.info('data:'+post_action)
                        #logger.info('post_request:'+post_request)
                except ( ConnectionError, Timeout, JSONDecodeError) as ce:
                    logger.error(ce)
            else:
                logger.warning("unkown change for "+str(triggeringID))
                logger.debug(current_response_content)


