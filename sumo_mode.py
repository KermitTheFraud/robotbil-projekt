import pwm
import ir_sens
import tof_sens
import time

def scan(): #Denne funktion kører bilen i ring og skanner for objekter
    while True:
        x = tof_sens.measure_dist_cm() #kalder tof_sens funktion. Den måler afstand i cm og gemmer den i variable x
        if x >= 50:
            pwm.stop_rotate_motor_right() #kalder pwm rotate_right. Den rotere til højre
        else:
            detect_corner()

def detect_corner(): #Denne funktion måler afstand mellem det ene hjørne og det andet
    cornerJumps = 1
    while tof_sens.measure_dist_cm() <= 60:
        pwm.stop_rotate_motor_right()
        cornerJumps += 1
        print(cornerJumps)
    halfJump = round(cornerJumps/2)
    for x in range(halfJump):
        pwm.stop_rotate_motor_left()
        print(x)
    headbutt()

def headbutt():  # Denne funktion accelerere og kører langsomt fremad.
    pwm.speed_up()  # kalder pwm funktion speed_up og kører med høj hastighed til objekt
    fastTime = 0
    while True:
        time.sleep(0.1)
        fastTime += 0.1
        x = tof_sens.measure_dist_cm()
        if x <= 8:  # hvis afstand x er < end et værdi
            slowTime = 0
            pwm.slow_down()  # Kalder pwm slow_down funktion. Kør langsomt frem
            dark_line(fastTime, slowTime)  # kalder næste funktion dark_line og overfører variablen start_time videre

def dark_line(fastTime, slowTime):
    while True:
        slowTime += 0.1
        time.sleep(0.1)
        if ir_sens.detect_light() >= ir_sens.set_point:
            pwm.motorBrems() #stop motor. Kalder pwm funktion stop_motor
            centrering(fastTime, slowTime)

def centrering(totalSlow, totalFast):# Denne funktion kører bilen baglæns tilbage til midten på samme tid som den kørte frem
    while True:
        pwm.driveBackSlow() #kalder pwm funktion drive_back
        print(totalSlow)
        time.sleep(totalSlow) #kalder funktion time.sleep() angiver forskellen mellem starttid og sluttid total_diff som argument
        pwm.driveBackFast()
        time.sleep(totalFast)
        pwm.stop_motor()
        scan() #kalder scan funktionen
