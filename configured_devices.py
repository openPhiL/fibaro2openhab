
configured_devices = { 
"""--------------Wohnzimmer---------------"""
#WohnzimmerFensterVorne
    '191' : {
            "value" : {
                "name" : 'WohnzimmerFensterVorneSensor_Position',
                "true" : "OPEN",
                    "false" : "CLOSED" } } ,
    '192' : {
            "value" : { 
                "name" :  'WohnzimmerFensterVorneSensor_Temperatur',
                "data" : { }  } },
#WohnzimmerFensterHinten
    '195' : {
            "value" : {
                "name" :  'WohnzimmerFensterHintenSensor_Position',
                "true" : "OPEN",
                "false" : "CLOSED" } } ,
    '196' : {
            "value" : { 
                "name" :  'WohnzimmerFensterHintenSensor_Temperatur',
                "data" : { }  } },
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
                "name" : 'Livingroom_Outlet_Refrigerator_MeterWatts' ,
                "data" : { }   } },

"""--------------UG Flur---------------"""
#UntergeschossVorneBewegungsmelder Vorne
    '115' : {
            "value" : {
                "name" :  'UntergeschossVorneBewegungsmelder_Bewegung',
                "true" : "ON",
                "false" : "OFF" } } ,
    '116' : { 
            "value" : { 
                "name" : 'UntergeschossVorneBewegungsmelder_Temperatur',
                "data" : { }   } },
    '117' : {  
            "value" : { 
                "name" : 'UntergeschossVorneBewegungsmelder_Helligkeit',
                "data" : { }   } },
#UntergeschossVorneBewegungsmelder Hinten
    '60' : {
            "value" : {
                "name" :  'UntergeschossHintenBewegungsmelder_Bewegung',
                "true" : "ON",
                "false" : "OFF" } } ,
    '61' : { 
            "value" : { 
                "name" : 'UntergeschossHintenBewegungsmelder_Temperatur',
                "data" : { }   } },
    '62' : { 
            "value" : { 
                "name" : 'UntergeschossHintenBewegungsmelder_Helligkeit',
                "data" : { }   } },

"""--------------WC---------------"""
#WCBewegungsmelders
    '5' : {
            "value" : {
                "name" :  'WCBewegungsmelder_Bewegung',
                "true" : "ON",
                "false" : "OFF" } } ,
    '6' : { 
            "value" : { 
                "name" : 'WCBewegungsmelder_Temperatur',
                "data" : { }   } },
    '7' : { 
            "value" : { 
                "name" : 'WCBewegungsmelder_Helligkeit',
                "data" : { }   } },


"""--------------Kitchen ---------------"""
#Kitchen_Outlet
    '113' : { 
            "energy" : { 
                "name" : 'Kitchen_Outlet_Coffeemachine_MeterWatts',
                "data" : { } } },
    '54'  : { 
            "energy" : { 
                "name" : 'Kitchen_Outlet_Refrigerator_MeterWatts', 
                "data" : { } } },
    '56'  : { 
            "energy" : { 
                "name" : 'Kitchen_Outlet_Freezer_MeterWatts',
                "data" : { } } },
    '113' : { 
            "power" : { 
                "name" : 'Kitchen_Outlet_Coffeemachine_MeterKWh',
                "data" : { } } },
    '54'  : { 
            "power" : { 
                "name" : 'Kitchen_Outlet_Refrigerator_MeterKWh',
                "data" : { } } },
    '56'  : { 
            "power" : { 
                "name" : 'Kitchen_Outlet_Freezer_MeterKWh',
                "data" : { } } },

"""--------------Essbereich---------------"""
#EssbereichBewegungsmelder
    '137' : {
            "value" : {
                "name" :  'EssbereichBewegungsmelder_Bewegung',
                "true" : "ON",
                "false" : "OFF" } } ,
    '138' : { 
            "value" : { 
                "name" : 'EssbereichBewegungsmelder_Temperatur',
                "data" : { }  } },
    '139' : { 
            "value" : { 
                "name" : 'EssbereichBewegungsmelder_Helligkeit',
                "data" : { }  } },
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
                "name" : 'KucheBewegungsmelderHinten_Temperatur',
                "data" : { } } }, 
    '139' : { 
            "value" : {
                "name" : 'KucheBewegungsmelderHinten_Helligkeit',
                "data" : { } } }, 

    '220' : {
            "value" : {
                "name" :  'KucheBewegungsmelderHinten_Bewegung',
                "true" : "ON",
                "false" : "OFF" } } ,
    '221' : { 
            "value" : { 
                "name" : 'KucheBewegungsmelderHinten_Temperatur' ,
                "data" : { } } }, 
    '222' : { 
            "value" : { 
                "name" : 'KucheBewegungsmelderHinten_Helligkeit',
                "data" : { } } }, 
#Outside_Devices
    '234' : { 
            "value" : { 
                "name" : 'AussenSensor_Temperatur'  ,
                "data" : { } } }, 
    '235' : { 
            "value" : { 
                "name" : 'AussenSensor_Helligkeit' ,
                "data" : { } } }, 
#Bathroom-Devices
    '131' : {
            "value" : {
                "name" :  'BadezimmerBewegungsmelderWanne_Bewegung',
                "true" : "ON",
                "false" : "OFF" } } ,
    '132' : { 
            "value" : { 
                "name" : 'BadezimmerBewegungsmelderWanne_Temperatur' ,
                "data" : { } } }, 

    '133' : { 
            "value" : { 
                "name" : 'BadezimmerBewegungsmelderWanne_Helligkeit'  ,
                "data" : { } } }, 

    '95' : {
            "value" : {
                "name" :  'BadezimmerBewegungsmelderWanne_Bewegung',
                "true" : "ON",
                "false" : "OFF"  } } ,
    '96' : { 
            "value" : { 
                "name" : 'BadezimmerBewegungsmelderWanne_Temperatur'  ,
                "data" : { } } }, 
    '97' : { 
            "value" : { 
                "name" : 'BadezimmerBewegungsmelderWanne_Helligkeit',
                "data" : { } } }, 
#Masterbedroom - Devices
    '11' : {
            "value" : {
                "name" :  'SchlafzimmerEingangBewegungsmelder_Bewegung',
                "true" : "ON",
                "false" : "OFF" } } ,
    '12' : { 
            "value" : { 
                "name" : 'SchlafzimmerEingangBewegungsmelder_Temperatur' ,
                "data" : { } } }, 
    '13' : { 
            "value" : { 
                "name" : 'SchlafzimmerEingangBewegungsmelder_Helligkeit' ,
                "data" : { } } }, 

#LukasBedroom -Devices
    '161' : {
        "actions" : {
            "value" : {
                "name" :  'LukasZimmer_SensorUntermBett_Bewegung',
                "true" : "ON",
                "false" : "OFF" } } } ,
    '162' : { 
            "value" : {
                "name" : 'LukasZimmer_SensorUntermBett_Temperatur',
                "data" : { } } }, 
    '163' : { 
            "value" : { 
                "name" : 'LukasZimmer_SensorUntermBett_Helligkeit',
                "data" : { } } }, 
    '164' : { 
            "value" : { 
                "name" : 'LukasZimmer_SensorUntermBett_Luftfeuchtigkeit',
                "data" : { } } }, 


#LeaBedroom-Devices

#Salon











}