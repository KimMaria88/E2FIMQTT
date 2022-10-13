

import paho.mqtt.client as mqtt
import time
#----------------------
#constans

HOSTADDRESS: str = 'localhost'
PORTNUMBER: int = 1883
KEEPALIVE: int = 60
TOPIC____: str = 'iot2022/name'
SLEEPTIME__: int = 10
#----------------------

#----------------------
#connect to server
client = mqtt.Client()
client.connect(HOSTADDRESS, PORTNUMBER, KEEPALIVE)

while True:
    massage: str = 'k:Mathäß'
    client.publish(TOPIC____, massage)
    print(massage)
    time.sleep(SLEEPTIME__)