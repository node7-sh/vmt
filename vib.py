import time
import os
import device_model0
import device_model1
import paho.mqtt.client as mqtt
import subprocess
import datetime
import csv

device0 = device_model0.DeviceModel("WTVB02", "/dev/ttyUSB0", 9600, 0x50); device0.openDevice(); device0.startLoopRead()
device1 = device_model1.DeviceModel("WTVB02", "/dev/ttyUSB1", 9600, 0x51); device1.openDevice(); device1.startLoopRead()

hostname = "test.mosquitto.org"     # MQTT Hostname
topic="my/topic/here/4711"          # MQTT Topic
intervall = 1.0                     # Intervall
next_start = time.time()

time.sleep(1)

while True:
    start = time.time()
    ts = str(int(time.time()))
    dt = datetime.datetime.utcnow().strftime("%Y-%m-%d %H:%M:%S")
    os.system('clear')
    var0 = ("vx:{} vy:{} vz:{} ax:{} ay:{} az:{} t:{} sx:{} sy:{} sz:{} fx:{} fy:{} fz:{}".format(device0.get("58"),device0.get("59"),device0.get("60"),device0.get("61"),device0.get("62"),device0.get("63"),device0.get("64"),device0.get("65"),device0.get("66"),device0.get("67"),device0.get("68"),device0.get("69"),device0.get("70")))
    var1 = ("vx:{} vy:{} vz:{} ax:{} ay:{} az:{} t:{} sx:{} sy:{} sz:{} fx:{} fy:{} fz:{}".format(device1.get("58"),device1.get("59"),device1.get("60"),device1.get("61"),device1.get("62"),device1.get("63"),device1.get("64"),device1.get("65"),device1.get("66"),device1.get("67"),device1.get("68"),device1.get("69"),device1.get("70")))
    varx = dt + "," + var0 + "," + var1 + "," + ts
#    print(varx)
    print(time.time()-next_start)
    next_start += intervall
    rest_zeit = next_start - time.time()

    response = subprocess.run(["ping", "-c1", „google.com“], capture_output=True, text=True)
    if response == 0:
        client = mqtt.Client(mqtt.CallbackAPIVersion.VERSION2)
        client.connect(hostname,1883,60)
        client.publish(topic,varx)
        client.disconnect()
    else:
        pass
    
    if rest_zeit > 0:
        time.sleep(rest_zeit)
    else:
        # Falls die Messung länger als geplant gedauert hat, wird ohne Pause weitergemacht
        # oder ggf. Fehlerbehandlung oder Logging hier einfügen.
        pass
