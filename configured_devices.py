
configured_devices = { 
###"""--------------Wohnzimmer---------------"""
#WohnzimmerFensterVorne
    '191' : {
            "value" : {
                "name" : 'WohnzimmerFensterVorneSensor_Position',
                "true" : "OPEN",
                "false" : "CLOSED" } } ,
    '192' : {
            "value" : { 
                "name" :  'WohnzimmerFensterVorneSensor_Temperatur' } },
#WohnzimmerFensterHinten
    '195' : {
            "value" : {
                "name" :  'WohnzimmerFensterHintenSensor_Position',
                "true" : "OPEN",
                "false" : "CLOSED" } } ,
    '196' : {
            "value" : { 
                "name" :  'WohnzimmerFensterHintenSensor_Temperatur' } },
#WohnzimmerFensterMitte
    '229' : {
            "value" : {
                "name" :  'WohnzimmerFensterMitteSensor_Position',
                "true" : "Gekippt",
                "false" : "Geschlossen" } } ,
    '231' : {
            "value" : {
                "name" :  'WohnzimmerFensterMitteSensor_Position',  
                "true" : "Offen",
                "false" : "Geschlossen" } } ,
#Livingroom_Outlet_Refrigerator
    '175' : { 
            "energy" : {
                "name" : 'Livingroom_Outlet_Refrigerator_MeterWatts' } },

###"""--------------UG Flur---------------"""
#UntergeschossVorneBewegungsmelder Vorne
    '115' : {
            "value" : {
                "name" :  'UntergeschossVorneBewegungsmelder_Bewegung',
                "true" : "ON",
                "false" : "OFF" } } ,
    '116' : { 
            "value" : { 
                "name" : 'UntergeschossVorneBewegungsmelder_Temperatur' } },
    '117' : {  
            "value" : { 
                "name" : 'UntergeschossVorneBewegungsmelder_Helligkeit'} },
#UntergeschossVorneBewegungsmelder Hinten
    '60' : {
            "value" : {
                "name" :  'UntergeschossHintenBewegungsmelder_Bewegung',
                "true" : "ON",
                "false" : "OFF" } } ,
    '61' : { 
            "value" : { 
                "name" : 'UntergeschossHintenBewegungsmelder_Temperatur' } },
    '62' : { 
            "value" : { 
                "name" : 'UntergeschossHintenBewegungsmelder_Helligkeit' } },

###"""--------------WC---------------"""
#WCBewegungsmelders
    '5' : {
            "value" : {
                "name" :  'WCBewegungsmelder_Bewegung',
                "true" : "ON",
                "false" : "OFF" } } ,
    '6' : { 
            "value" : { 
                "name" : 'WCBewegungsmelder_Temperatur'} },
    '7' : { 
            "value" : { 
                "name" : 'WCBewegungsmelder_Helligkeit' } },


###"""--------------Kitchen ---------------"""

#Kitchen_Outlet
    '113' : { 
            "energy" : { 
                "name" : 'Kuche_Kaffeemaschine_MeterWatts' },
            "power" : { 
                "name" : 'Kuche_Kaffeemaschine_MeterKWh' } },
    '54'  : { 
            "energy" : { 
                "name" : 'Kitchen_Outlet_Refrigerator_MeterWatts' } ,
            "power" : { 
                "name" : 'Kitchen_Outlet_Refrigerator_MeterKWh' } 
                },
    '56'  : { 
            "energy" : { 
                "name" : 'Kitchen_Outlet_Freezer_MeterWatts' },
            "power" : { 
                "name" : 'Kitchen_Outlet_Freezer_MeterKWh' } },

###"""--------------Essbereich---------------"""
#EssbereichBewegungsmelder
    '137' : {
            "value" : {
                "name" :  'EssbereichBewegungsmelder_Bewegung',
                "true" : "ON",
                "false" : "OFF" } } ,
    '138' : { 
            "value" : { 
                "name" : 'EssbereichBewegungsmelder_Temperatur'} },
    '139' : { 
            "value" : { 
                "name" : 'EssbereichBewegungsmelder_Helligkeit'} },
    '210' : {
            "value" : {
                "name" :  'ErdgeschossFensterHintenTuereSensor_Position',
                "true" : "Gekippt",
                "false" : "Geschlossen" } } ,
    '212' : {
            "value" : {
                "name" :  'ErdgeschossFensterHintenTuereSensor_Position',
                "true" : "Offen",
                "false" : "Geschlossen" } } ,
#Flur - Devices
    '214' : {
            "value" : {
                "name" :  'KucheBewegungsmelderHinten_Bewegung',
                "true" : "ON",
                "false" : "OFF" } } ,
    '138' : { 
            "value" : { 
                "name" : 'KucheBewegungsmelderHinten_Temperatur'} }, 
    '139' : { 
            "value" : {
                "name" : 'KucheBewegungsmelderHinten_Helligkeit' } }, 

    '220' : {
            "value" : {
                "name" :  'KucheBewegungsmelderHinten_Bewegung',
                "true" : "ON",
                "false" : "OFF" } } ,
    '221' : { 
            "value" : { 
                "name" : 'KucheBewegungsmelderHinten_Temperatur' } }, 
    '222' : { 
            "value" : { 
                "name" : 'KucheBewegungsmelderHinten_Helligkeit' } }, 
#Outside_Devices
    '234' : { 
            "value" : { 
                "name" : 'AussenSensor_Temperatur'   } }, 
    '235' : { 
            "value" : { 
                "name" : 'AussenSensor_Helligkeit'  } }, 
#Bathroom-Devices
    '131' : {
            "value" : {
                "name" :  'BadezimmerBewegungsmelderWanne_Bewegung',
                "true" : "ON",
                "false" : "OFF" } } ,
    '132' : { 
            "value" : { 
                "name" : 'BadezimmerBewegungsmelderWanne_Temperatur' } }, 

    '133' : { 
            "value" : { 
                "name" : 'BadezimmerBewegungsmelderWanne_Helligkeit' } }, 

    '95' : {
            "value" : {
                "name" :  'BadezimmerBewegungsmelderWanne_Bewegung',
                "true" : "ON",
                "false" : "OFF"  } } ,
    '96' : { 
            "value" : { 
                "name" : 'BadezimmerBewegungsmelderWanne_Temperatur' } }, 
    '97' : { 
            "value" : { 
                "name" : 'BadezimmerBewegungsmelderWanne_Helligkeit' } }, 
#Masterbedroom - Devices
    '11' : {
            "value" : {
                "name" :  'SchlafzimmerEingangBewegungsmelder_Bewegung',
                "true" : "ON",
                "false" : "OFF" } } ,
    '12' : { 
            "value" : { 
                "name" : 'SchlafzimmerEingangBewegungsmelder_Temperatur'  } }, 
    '13' : { 
            "value" : { 
                "name" : 'SchlafzimmerEingangBewegungsmelder_Helligkeit' } }, 

#LukasBedroom -Devices
    '161' : {
            "value" : {
                "name" :  'LukasZimmer_SensorUntermBett_Bewegung',
                "true" : "ON",
                "false" : "OFF" } } ,
    '162' : { 
            "value" : {
                "name" : 'LukasZimmer_SensorUntermBett_Temperatur'} }, 
    '163' : { 
            "value" : { 
                "name" : 'LukasZimmer_SensorUntermBett_Helligkeit' } }, 
    '164' : { 
            "value" : { 
                "name" : 'LukasZimmer_SensorUntermBett_Luftfeuchtigkeit'} }, 


#LeaBedroom-Devices

#Salon











}