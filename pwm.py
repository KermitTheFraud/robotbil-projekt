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


def stop_motor(): #Denne funktion stopper motoren

def stop_rotate_motor_right():

def stop_rotate_motor_left():

def speed_up(): #Denne funktion accelerere motoren

def slow_down(): #Denne funktion sænker hastigheden af motoren

def drive_back(): #Denne funktion får motoren til at kører baglæns

def forward_turn_left(): #Denne funktion får motoren til at kører lige ud og dreje til venstre

def forward_turn_right(): #Denne funktion får motoren til at kører lige ud også deje til højre

def rotate_right(): #Denne funktion får motoren til at kører i ring fra højre side
def rotate_left()
