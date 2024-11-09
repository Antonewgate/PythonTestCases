import threading
import time
import random

BCM_info = {"ID":0x123, "Channel":1, "DLC":1,"Data":{"VehicleSpeed":0}}
Period = 0.25
SpeedSample = []
index = 0
while index in range(0,10):
    SpeedSample.append(random.randint(0,250))
    index+=1

def TransmitMsg():
    print(BCM_info)
    threading.Timer(Period,TransmitMsg).start()

TransmitMsg()

print("soy")
printo("segundo soy")
