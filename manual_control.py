import wall_follow
import sumo_mode
import netværk
import tof_sens
from utime import sleep

def sumoTest():
    sleep(3)
    sumo_mode.scan()

def wallFollow_test():
    sleep(3)
    wall_follow.measure_dist()

def modeSelectTest():
    if tof_sens.measure_dist_cm() <= 10:
        sumoTest()
    else:
        wallFollow_test()