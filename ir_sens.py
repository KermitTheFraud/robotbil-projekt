from machine import Pin, ADC
from time import sleep
refl_sens = ADC(Pin(26))
volt = 3.3
max_range = 65335.0
set_point = 3.1

def detect_light():  #funktionen dektektere om sensor kører på en lys overflade eller sort
    while True:
        refl_value = refl_sens.read_u16()
        voltage_value = refl_value * (volt / max_range)
        if voltage_value >= set_point:
            return voltage_value
        elif voltage_value <= set_point:
            return voltage_value






