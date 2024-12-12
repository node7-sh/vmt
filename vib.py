import time
import os
import device_model0
import device_model1
import paho.mqtt.client as mqtt
import subprocess
import datetime

device0 = device_model0.DeviceModel("WTVB02", "/dev/ttyUSB0", 9600, 0x50)
device0.openDevice()
device0.startLoopRead()
device1 = device_model1.DeviceModel("WTVB02", "/dev/ttyUSB1", 9600, 0x51)
device1.openDevice()
device1.startLoopRead()

#MQTT Hostname
hostname = "test.mosquitto.org"
#MQTT Topic
topic="test/topic"

time.sleep(1)

while True:
#    time.sleep(1)
    ts = str(int(time.time()))
    dt = datetime.datetime.utcnow().strftime("%Y-%m-%d %H:%M:%S")
#    os.system('clear')
#    var1 = ("vx:{} vy:{} vz:{} ax:{} ay:{} az:{} t:{} sx:{} sy:{} sz:{} fx:{} fy:{} fz:{}".format(device.get("58"),device.get("59"),device.get("60"),device.get("61"),device.get("62"),device.get("63"),device.get("64"),device.get("65"),device.get("66"),device.get("67"),device.get("68"),device.get("69"),device.get("70")))
    var0 = ("{},{},{}".format(device0.get("58"),device0.get("59"),device0.get("60")))
    var1 = ("{},{},{}".format(device1.get("58"),device1.get("59"),device1.get("60")))
    varx = dt + "," + var0 + "," + var1 + "," + ts
#    print(varx)

    response = os.system("ping -c 1 " + "google.com")
    if response == 0:
        client = mqtt.Client(mqtt.CallbackAPIVersion.VERSION2)
        client.connect(hostname,1883,60)
        client.publish(topic,varx)
        client.disconnect()
#    else:
#        time.sleep(0.1)

    time.sleep(0.8)
