import paho.mqtt.client as mqtt
import time
import datetime
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
    german_date_format = " %H:%M:%S"
    time_obj = datetime.datetime.now()
    massage: str = (time_obj.strftime(german_date_format))
    client.publish(TOPIC____, massage)
    print(massage)
    time.sleep(SLEEPTIME__)