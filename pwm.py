from machine import Pin, PWM
from time import sleep

# Initialiserer PWM (Pulse Width Modulation) for venstre motor fremad
left_motor_frem = PWM(Pin(1))  # Opretter en PWM forbindelse på pin 1 til venstre motor fremad

# Initialiserer PWM for venstre motor tilbage
left_motor_tilbage = PWM(Pin(0))  # Opretter en PWM forbindelse på pin 0 til venstre motor tilbage

# Initialiserer PWM for højre motor fremad
right_motor_frem = PWM(Pin(3))  # Opretter en PWM forbindelse på pin 3 til højre motor fremad

# Initialiserer PWM for højre motor tilbage
right_motor_tilbage = PWM(Pin(2))  # Opretter en PWM forbindelse på pin 2 til højre motor tilbage

# Sætter frekvens for motorene
left_motor_frem.freq(1000)
left_motor_tilbage.freq(1000)
right_motor_frem.freq(1000)
right_motor_tilbage.freq(1000)

# Funktionen som sætter dutycycles på en given pwm, til en angivet procent
def setDutyPercent(PWMVar, changeVal):
    PWMVar.duty_u16(int((65535/100)*changeVal))

def stop_motor(): #Denne funktion stopper motoren
    setDutyPercent(left_motor_frem, 0)
    setDutyPercent(left_motor_tilbage, 0)
    setDutyPercent(right_motor_frem, 0)
    setDutyPercent(right_motor_tilbage, 0)
    sleep(0.1)

def stop_rotate_motor_right():
    setDutyPercent(left_motor_tilbage, 0)
    setDutyPercent(right_motor_frem, 0)
    setDutyPercent(left_motor_frem, 23.8)
    setDutyPercent(right_motor_tilbage, 30)
    sleep(0.1)
    setDutyPercent(left_motor_frem, 0)
    setDutyPercent(right_motor_tilbage, 0)
    sleep(0.1)

def stop_rotate_motor_left():
    setDutyPercent(left_motor_frem, 0)
    setDutyPercent(right_motor_tilbage, 0)
    setDutyPercent(left_motor_tilbage, 23.8)
    setDutyPercent(right_motor_frem, 30)
    sleep(0.1)
    setDutyPercent(left_motor_tilbage, 0)
    setDutyPercent(right_motor_frem, 0)
    sleep(0.1)

def speed_up(): #Denne funktion accelerere motoren
    setDutyPercent(left_motor_tilbage, 0)
    setDutyPercent(right_motor_tilbage, 0)
    setDutyPercent(left_motor_frem, 53.8)
    setDutyPercent(right_motor_frem, 60)
    sleep(0.1)

def slow_down(): #Denne funktion sænker hastigheden af motoren
    setDutyPercent(left_motor_frem, 0)
    setDutyPercent(right_motor_frem, 0)
    setDutyPercent(left_motor_tilbage, 53.8)
    setDutyPercent(right_motor_tilbage, 60)
    sleep(0.2)
    setDutyPercent(left_motor_frem, 23.8)
    setDutyPercent(right_motor_frem, 30)
    sleep(0.1)

def driveBackFast(): #Denne funktion får motoren til at kører baglæns
    setDutyPercent(left_motor_frem, 0)
    setDutyPercent(right_motor_frem, 0)
    setDutyPercent(left_motor_tilbage, 53.8)
    setDutyPercent(right_motor_tilbage, 60)
    sleep(0.1)

def driveBackSlow():
    setDutyPercent(left_motor_frem, 0)
    setDutyPercent(right_motor_frem, 0)
    setDutyPercent(left_motor_tilbage, 23.8)
    setDutyPercent(right_motor_tilbage, 30)
    sleep(0.1)

def motorBrems():
    setDutyPercent(left_motor_frem, 0)
    setDutyPercent(right_motor_frem, 0)
    setDutyPercent(left_motor_tilbage, 53.8)
    setDutyPercent(right_motor_tilbage, 60)
    sleep(0.1)
    setDutyPercent(left_motor_tilbage, 0)
    setDutyPercent(right_motor_tilbage, 0)


#def turn_left(): #Denne funktion får motoren til at dreje til venstre

#def turn_right(): #Denne funktion får motoren til at deje til højre

#def rotate_right(): #Denne funktion får motoren til at kører i ring fra højre side

#def rotate_left():
