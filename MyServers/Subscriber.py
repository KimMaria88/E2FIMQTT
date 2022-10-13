import paho.mqtt.client as mqtt
import time
import datetime
import socket
import uuid
#----------------------
#constans

HOSTADDRESS: str = 'localhost'
PORTNUMBER: int = 1883
KEEPALIVE: int = 60
TOPIC____: str = 'iot2022/test'
SLEEPTIME__: int = 10
#----------------------

def on_message(client, userdata, msg):
    print("Topic:  " + msg.topic)
    lol: str = msg.payload.decode('UTF-8')
    print('Data:' + lol)

#----------------------
#connect to server
client = mqtt.Client()
client.on_message = on_message
client.connect(HOSTADDRESS, PORTNUMBER, KEEPALIVE)
client.subscribe(TOPIC____)

client.loop_forever()