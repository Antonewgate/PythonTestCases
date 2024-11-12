import threading
import time
import random
print("just 1 hour to change the world")
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

print("esta es la version 1")

for item in range(1):
    print(f"este es el 4to commit pero priemra modificacion")

print("modificandolo un poco")


class numero():
    def __init__(self, nom):
        self.nommbre= nom
        self.profesion = "ingeniero"

uno = numero("tony")
print(uno.nommbre)
print("ya aparecio el merge")
