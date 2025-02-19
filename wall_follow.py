import pwm
import tof_sens
from utime import sleep

lowerRange = 30
higherRange = 40

def default_position(): #Denne funktion holder bilen indenfor en bestemt rækkevide
    pwm.wallDrive()#motoren kører forlæns, kald pwm funktion
    while True:
        x = tof_sens.measure_dist_cm()
        if x >= higherRange:
            turn_right()
        elif x <= lowerRange:
            turn_left()

def turn_right():
    while True:
        x = tof_sens.measure_dist_cm()#kald tof_sens. Start måling og gem værdien i en variable kaldet x
        closerVal = x - higherRange
        if closerVal >= 40:
            closerVal = 40
        if x >= higherRange + 15:
            pwm.leftWallLook()
            sleep(0.2)
            x = tof_sens.measure_dist_cm()
            if x >= higherRange + 25:
                findWallR()
                return
        elif x <= higherRange: #hvis x er indenfor den ønskede værdi kald default_position
            pwm.wallDrive()
            return
        pwm.turn_right(closerVal)  # kald pwm funktion. Det sender en signal til motoren om at den skal dreje til højre


def turn_left():
    while True:
        x = tof_sens.measure_dist_cm()  # kald tof_sens. Start måling og gem værdien i en variable kaldet x
        farVal = lowerRange - x
        if x <= 15:
            print("go left")
            findWallL(farVal)
            break
        elif x >= lowerRange:  # hvis x er indenfor den ønskede værdi kald default_position
            pwm.wallDrive()
            return
        pwm.turn_left(farVal)  # kald pwm funktion. Det sender en signal til motoren om at den skal dreje til højre


def findWallR(): #Denne funktion får bilen til at dreje skarpt til højre
    sleep(1)
    while True:
        pwm.wallFindR()
        if tof_sens.measure_dist_cm() <= higherRange + 15:
            pwm.wallDrive()
            return

def findWallL(farVal):
    exponent = 0
    while True:
        if tof_sens.measure_dist_cm() <= 8:
            print("near crash")
            crashPreventor()
            return
        pwm.sharpLeft(exponent)
        oldVal = farVal
        farVal = tof_sens.measure_dist_cm()
        exponent += 2
        if farVal >= oldVal + 1:
            pwm.wallDrive()
            break

def crashPreventor():
    dist = tof_sens.measure_dist_cm()
    while dist <= 8:
        pwm.wallFindL()
        dist = tof_sens.measure_dist_cm()
    pwm.wallDrive()
    return