import time
import os
import device_model0
import device_model1
import varvib
import paho.mqtt.client as mqtt
import subprocess
import datetime
import csv

device0 = device_model0.DeviceModel("WTVB02", "/dev/ttyUSB0", 9600, 0x50); device0.openDevice(); device0.startLoopRead()
device1 = device_model1.DeviceModel("WTVB02", "/dev/ttyUSB1", 9600, 0x51); device1.openDevice(); device1.startLoopRead()

hostname = varvib.mqtt_host
topic = varvib.mqtt_topic
interval = varvib.interval
next_start = time.time()

time.sleep(1)

while True:
    start = time.time(); ts = str(int(time.time())); dt = datetime.datetime.utcnow().strftime("%Y-%m-%d %H:%M:%S")
    var0 = ("vx0:{},vy0:{},vz0:{},ax0:{},ay0:{},az0:{},t0_c:{},sx0:{},sy0:{},sz0:{},fx0:{},fy0:{},fz0:{}".format(device0.get("58"),device0.get("59"),device0.get("60"),device0.get("61"),device0.get("62"),device0.get("63"),device0.get("64"),device0.get("65"),device0.get("66"),device0.get("67"),device0.get("68"),device0.get("69"),device0.get("70")))
    var1 = ("vx1:{},vy1:{},vz1:{},ax1:{},ay1:{},az1:{},t1_c:{},sx1:{},sy1:{},sz1:{},fx1:{},fy1:{},fz1:{}".format(device1.get("58"),device1.get("59"),device1.get("60"),device1.get("61"),device1.get("62"),device1.get("63"),device1.get("64"),device1.get("65"),device1.get("66"),device1.get("67"),device1.get("68"),device1.get("69"),device1.get("70")))
#    print(time.time()-next_start)
    next_start += interval; rest_zeit = next_start - time.time()
    varx = dt + "," + var0 + "," + var1 + "," + ts + "," + str(interval) + "," + str(rest_zeit)

    response = response = os.system("ping -c 1 " + "google.com  > /dev/null 2>&1")
    if response == 0:
        client = mqtt.Client(mqtt.CallbackAPIVersion.VERSION2)
        client.connect(hostname,1883,60)
        client.publish(topic,varx)
        client.disconnect()
    else:
        pass
#    print(rest_zeit)
    if rest_zeit > 0:
        time.sleep(rest_zeit)
    else:
        # Case it takes longer than Intervall the process goes on regular.
        # If necessary you can LOG or do anything else. Send message or whatever.
        pass
