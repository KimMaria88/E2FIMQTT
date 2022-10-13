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
TOPIC____: str = 'iot2022/input'
SLEEPTIME__: int = 10
#----------------------

#----------------------
#connect to server
client = mqtt.Client()
client.connect(HOSTADDRESS, PORTNUMBER, KEEPALIVE)

while True:
    message: str = hex(uuid.getnode()).replace('0x', '').upper()
    message = ':'.join(message[i: i + 2] for i in range(0, 11, 2))
    client.publish(TOPIC____, message)
    print(message)
    time.sleep(SLEEPTIME__)
