import pwm
import tof_sens


def measure_dist(): # Denne funktion måler start afstand mellem væggen og bilen

#måler afstand i cm ved at kalde på tof-sens og gemmer det målte distance i en variable kaldet x

#kald default_position. X det målte afstand bliver overført til næste funktion default_position

def default_position(): #Denne funktion holder bilen indenfor en bestemt rækkevide

#motoren kører forlæns, kald pwm funktion

#hvis x er større end værdi kald turn_right funktion

#hvis x er mindre end værdi kald turn_left funktion

#hvis x er meget større end f.eks. 20 cm kald sharp_turn_right

#hvis x er meget mindre end f.eks. 7-10 kald sharp turn_left


def turn_right():
#kald pwm funktion. Det sender en signal til motoren om at den skal dreje til højre

#kald tof_sens. Start måling og gem værdien i en variable kaldet x

#hvis x er indenfor den ønskede værdi kald default_position

def turn_left():
#kalder pwm funktion. Det sender en signal til motoren om at den skal dreje til venstre

#kalder tof_sens. Det måler afstand i cm gemmer det en i variable kaldet x

#hvis x er indenfor den ønskede værdi kald default_position

def sharp_turn_right(): #Denne funktion får bilen til at dreje skarpt til højre

#kald pwm funktion. Det sender en signal til motoren om at den skal dreje til højre

#kald tof_sens. Det måler den nuværende afstand og gemmer det i en variable kaldet x

#hvis x er en indenfor den ønskede værdi kald default_position

def sharp_turn_left(): #Denne funktion

#kald pwm funktion. Det sender en signal til motoren om at den skal dreje til venstre

#kald tof_sens. Det måler nuværende afstand cm og gemmer det i en variable kaldet x

#hvis x er en indenfor den ønskede værdi kald default_position




