from machine import Pin
from time import sleep

refl_sens = Pin(14, Pin.IN)

def detect_light():  #funktionen dektektere om sensor kører på en lys overflade
    while True:
        if refl_sens == 0:




def detect_dark_line():  #funktionen dektektere om sensor kører på en sort overfalde/linje
    while True:
        if refl_sens == 1:





