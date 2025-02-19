import pwm
import ir_sens
import tof_sens
import time

cornerJumps = 0

def scan():  # Denne funktion kører bilen i ring og skanner for objekter
    global cornerJumps
    y = tof_sens.measure_dist_cm()
    while True:
        x = tof_sens.measure_dist_cm()  # kalder tof_sens funktion. Den måler afstand i cm og gemmer den i variable x
        if x >= 80 and y >= 80:
            pwm.stop_rotate_motor_right()  # kalder pwm rotate_right. Den rotere til højre
            y = x
        else:
            detect_corner()
            if cornerJumps >= 1:
                cornerJumps = 0
                headbutt()


def detect_corner():  # Denne funktion måler afstand mellem det ene hjørne og det andet
    global cornerJumps
    cornerJumps = 1
    while tof_sens.measure_dist_cm() <= 90:
        pwm.stop_rotate_motor_right()
        cornerJumps += 1
    halfJump = round(cornerJumps / 2)
    for x in range(halfJump):
        pwm.stop_rotate_motor_left()
    return


def headbutt():  # Denne funktion accelerere og kører langsomt fremad samt detektere om det kører på en sort overflade
    pwm.speed_up()  # kalder pwm funktion speed_up og kører med høj hastighed til objekt
    fastTime = 0
    while True:
        time.sleep(0.1)
        fastTime += 0.1
        x = tof_sens.measure_dist_cm()
        darkFound = ir_sens.detect_light()
        if darkFound >= ir_sens.set_point:
            pwm.stop_motor()  # stop motor. Kalder pwm funktion stop_motor
            centrering(0.1, fastTime)
            return
        elif x <= 20 or fastTime == 0.8:  # hvis afstand x er < end et værdi
            pwm.slow_down()  # Kalder pwm slow_down funktion. Kør langsomt frem
            dark_line(fastTime)  # kalder næste funktion dark_line og overfører variablen start_time videre
            return


def dark_line(fastTime):
    slowTime = 0
    while True:
        time.sleep(0.1)
        if slowTime >= 0.5:
            slowTime += 0.1
        if ir_sens.detect_light() >= ir_sens.set_point:
            pwm.stop_motor()  # stop motor. Kalder pwm funktion stop_motor
            centrering(slowTime, fastTime)
            return


def centrering(totalSlow, totalFast):  # Denne funktion kører bilen baglæns tilbage til midten på samme tid som den kørte frem
    pwm.driveBackSlow()  # kalder pwm funktion drive_back
    time.sleep(totalSlow)  # kalder funktion time.sleep() angiver forskellen mellem starttid og sluttid total_diff som argument
    pwm.stop_motor()
    pwm.driveBackFast()
    time.sleep(totalFast)
    pwm.stop_motor()
    for x in range(2):
        pwm.stop_rotate_motor_right()
    return
