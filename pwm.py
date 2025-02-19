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
    setDutyPercent(left_motor_frem, 28.3)
    setDutyPercent(right_motor_tilbage, 30)
    sleep(0.1)
    setDutyPercent(left_motor_frem, 0)
    setDutyPercent(right_motor_tilbage, 0)
    sleep(0.1)

def stop_rotate_motor_left():
    setDutyPercent(left_motor_frem, 0)
    setDutyPercent(right_motor_tilbage, 0)
    setDutyPercent(left_motor_tilbage, 28.3)
    setDutyPercent(right_motor_frem, 30)
    sleep(0.1)
    setDutyPercent(left_motor_tilbage, 0)
    setDutyPercent(right_motor_frem, 0)
    sleep(0.1)

def speed_up(): #Denne funktion accelerere motoren
    setDutyPercent(left_motor_tilbage, 0)
    setDutyPercent(right_motor_tilbage, 0)
    setDutyPercent(left_motor_frem, 38.3)
    setDutyPercent(right_motor_frem, 40)

def slow_down(): #Denne funktion sænker hastigheden af motoren
    setDutyPercent(left_motor_frem, 0)
    setDutyPercent(right_motor_frem, 0)
    setDutyPercent(left_motor_tilbage, 28.3)
    setDutyPercent(right_motor_tilbage, 30)
    sleep(0.2)
    setDutyPercent(left_motor_tilbage, 0)
    setDutyPercent(right_motor_tilbage, 0)
    setDutyPercent(left_motor_frem, 28.3)
    setDutyPercent(right_motor_frem, 30)
    sleep(0.1)

def driveBackFast(): #Denne funktion får motoren til at kører baglæns
    setDutyPercent(left_motor_frem, 0)
    setDutyPercent(right_motor_frem, 0)
    setDutyPercent(left_motor_tilbage, 38.3)
    setDutyPercent(right_motor_tilbage, 40)
def driveBackSlow():
    setDutyPercent(left_motor_frem, 0)
    setDutyPercent(right_motor_frem, 0)
    setDutyPercent(left_motor_tilbage, 28.3)
    setDutyPercent(right_motor_tilbage, 30)

def wallDrive():
    setDutyPercent(left_motor_tilbage, 0)
    setDutyPercent(right_motor_tilbage, 0)
    setDutyPercent(left_motor_frem, 33.3)
    setDutyPercent(right_motor_frem, 35)

def turn_right(closerVal):
    setDutyPercent(left_motor_frem, 33.3 + closerVal)

def turn_left(fartherVal):
    setDutyPercent(right_motor_frem, 40 + fartherVal)

def wallFindR():
    setDutyPercent(left_motor_tilbage, 0)
    setDutyPercent(right_motor_frem, 0)
    setDutyPercent(left_motor_frem, 28.3)
    setDutyPercent(right_motor_tilbage, 30)
    sleep(0.1)
    setDutyPercent(left_motor_frem, 0)
    setDutyPercent(right_motor_tilbage, 0)
    sleep(0.1)

def wallFindL():
    setDutyPercent(left_motor_frem, 0)
    setDutyPercent(right_motor_tilbage, 0)
    setDutyPercent(left_motor_tilbage, 28.3)
    setDutyPercent(right_motor_frem, 30)

def leftWallLook():
    setDutyPercent(left_motor_tilbage, 0)
    setDutyPercent(right_motor_tilbage, 0)
    setDutyPercent(left_motor_frem, 40)
    setDutyPercent(right_motor_frem, 27)

def sharpLeft(exponent):
    setDutyPercent(left_motor_tilbage, 0)
    setDutyPercent(right_motor_tilbage, 0)
    setDutyPercent(left_motor_frem, 28.3)
    setDutyPercent(right_motor_frem, 40 + exponent)