import pwm
import ir_sens
import tof_sens
import time

def scan(): #Denne funktion kører bilen i ring og skanner for objekter
    while True:
        x = tof_sens.measure_dist_cm() #kalder tof_sens funktion. Den måler afstand i cm og gemmer den i variable x
        if x >= 40:
            pwm.rotate_right() #kalder pwm rotate_right. Den rotere til højre
        else:
            detect_corner()

#hvis x er større > end et værdi

#kalder pwm modul, funktion rotate_right. Bliver ved med at rotere

#hvis x er mindre < end et værdi, stop

#kalder pwm stop_motor funktion. Bilen stopper med at rotere

def detect_corner(): #Denne funktion måler afstand mellem det ene hjørne og det andet
    cornerJumps = 1
    while tof_sens.measure_dist_cm() <= 40:
        pwm.rotate_right()
        cornerJumps += 1
        print(cornerJumps)
    halfJump = round(cornerJumps/2)

    for x in range(halfJump):
        pwm.rotate_left()
        print(x)

#hvis x er end værdi

#Start måling

#Når den måler en længere afstand stopper måling og motoren

#Finder midtpunktet ved at dividere med 2

#Kører til venstre til midtpunktet

#Stop motoren

def headbutt(): # Denne funktion accelerere og kører langsomt fremad samt detektere om det kører på en sort overflade
    x = tof_sens.measure_dist_cm()
    while True:
        if x > ??:  #kalder tof_sens funktion som måler afstand i cm gemmer den i en variable x
            pwm.speed_up() #kalder pwm funktion speed_up og kører med høj hastighed til objekt
            start_time = time.ticks_us() #kalder funktion time.tick_us og gemmer den i variable starttime.
        elif x < ???: #hvis afstand x er < end et værdi
            tof_sens.stop_measuring() #kalder tof_sens. Stop måling
            pwm.slow_down() #kalder pwm slow_down funktion. Kør langsomt frem
            dark_line(start_time) #kalder næste funktion dark_line og overfører variablen start_time videre


def dark_line(start_time):

    while True:
       if ir_sens.detect_dark_line() == True: #kalder ir_sens funktion. Hvis ir_sens dektekere en sort overflade == True
           pwm.stop_motor() #stop motor. Kalder pwm funktion stop_motor
           stop_time = time.ticks_us() #Stop tiden. Kalder time.tick_us() funktion og gemmer den i en variable stop_time
           total_diff = time.ticks_diff(start_time, stop_time) #kalder time.tick_diff(Beregner forskellen mellem start_time og stop_time) og gemmer den i en variable total_time
       elif ir_sens.detect_light() == True: #hvis ir_sens dektektere en hvid overflade == False
            pwm.slow_down() #kalder pwm slow_down funktion også forsætter den med at kører langsom frem
            centrering(total_diff) #total_time bliver overført til den næste funktion centrering




def centrering(total_diff):# Denne funktion kører bilen baglæns tilbage til midten på samme tid som den kørte frem

    while True:
        pwm.drive_back() #kalder pwm funktion drive_back
        time.sleep(total_diff) #kalder funktion time.sleep() angiver total_diff som argument
        scan() #kalder scan funktionen







