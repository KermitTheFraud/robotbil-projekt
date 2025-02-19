from machine import Pin
from utime import sleep
import time

pwmSensor = Pin(15, Pin.IN)


def measure_dist_cm():
    while pwmSensor.value() == 1:
        pass
    while pwmSensor.value() == 0:
        pass
    startTime = time.ticks_us()
    while pwmSensor.value() == 1:
        pass
    endTime = time.ticks_us()
    activeTime = time.ticks_diff(endTime, startTime)
    return activeTime/100

def measure_dist_mm():
    while pwmSensor.value() == 1:
        pass
    while pwmSensor.value() == 0:
        pass
    startTime = time.ticks_us()
    while pwmSensor.value() == 1:
        pass
    endTime = time.ticks_us()
    activeTime = time.ticks_diff(endTime, startTime)
    sleep(0.1)
    return activeTime/10

#def estimate_distance(): #wall-follow

