# publisher
import paho.mqtt.client as mqtt
import json
import time

client = mqtt.Client()
client.connect('192.168.0.106', 1883)

data = {'name' : '24:62:AB:B5:C4:C4',
       'age'  : '25',
       'id'   : '123'}
data1=json.dumps(data)

while True:
##    client.publish("LINTANGtopic/test", input('Message : '))
    
    client.publish("LINTANGtopic/test", data1)

    time.sleep(5)
