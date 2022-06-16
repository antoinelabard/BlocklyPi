################ Imports #################################
from time import *
from robotMotor import RobotMotor
import RPi.GPIO as GPIO


#####  definition des pins#####
led_pin = 23
bouton_pin = 24

etat_l = 0

GPIO.setmode(GPIO.BCM)

# Definition des pins en entree / sortie
GPIO.setup(bouton_pin, GPIO.IN, pull_up_down = GPIO.PUD_UP)
GPIO.setup(led_pin, GPIO.OUT)

# set of constants used to replace the motor numbers by more meaningful names

pouce_b = RobotMotor(0, 0, 130, 80)
pouce = RobotMotor(1, 50, 180, 180)
index = RobotMotor(2, 0, 180, 180)
majeur = RobotMotor(3, 0, 160, 0)
annulaire_auriculaire = RobotMotor(4, 0, 180, 0)
#main = RobotMotor(5, 0, 180, 90)
'''
a = RobotMotor(0, 0, 180)
b = RobotMotor(1, 0, 180)
c = RobotMotor(2, 0, 180)
d = RobotMotor(3, 0, 180)

e = RobotMotor(4, 0, 180)
f = RobotMotor(5, 0, 180)
g = RobotMotor(6, 0, 180)
h = RobotMotor(7, 0, 180)  #

i = RobotMotor(8, 0, 180)
j = RobotMotor(9, 0, 180)
k = RobotMotor(10, 0, 180)  #
l = RobotMotor(11, 0, 180)  #

m = RobotMotor(12, 0, 180)
n = RobotMotor(13, 0, 180)
o = RobotMotor(14, 0, 180)
p = RobotMotor(15, 0, 180)  '''

########################################################################

########### fonctions du bras robot #####################
'''
def reset_position():
    RobotMotor.set_motor_position(a, 80)
    RobotMotor.set_motor_position(b, 180)
    RobotMotor.set_motor_position(c, 180)
    RobotMotor.set_motor_position(d, 0)
    RobotMotor.set_motor_position(e, 0)
    #RobotMotor.set_motor_position(main, 90)
       
def position():
    RobotMotor.set_motor_position(a, 0)
    RobotMotor.set_motor_position(b, 50)
    RobotMotor.set_motor_position(c, 0)
    RobotMotor.set_motor_position(d, 160)
    RobotMotor.set_motor_position(e, 180)
    #RobotMotor.set_motor_position(main, 0)
'''


def reset_position():
    RobotMotor.set_motor_position(pouce_b, 80)
    RobotMotor.set_motor_position(pouce, 180)
    RobotMotor.set_motor_position(index, 180)
    RobotMotor.set_motor_position(majeur, 0)
    RobotMotor.set_motor_position(annulaire_auriculaire, 0)
    #RobotMotor.set_motor_position(main, 90)
       
def position():
    RobotMotor.set_motor_position(pouce_b, 0)
    RobotMotor.set_motor_position(pouce, 50)
    RobotMotor.set_motor_position(index, 0)
    RobotMotor.set_motor_position(majeur, 160)
    RobotMotor.set_motor_position(annulaire_auriculaire, 180)
    #RobotMotor.set_motor_position(main, 0)


def marcher():
    position()
    sleep(1)
    reset_position()
    sleep(1)
        
    
 
def un():
    position()
    sleep(2)
    RobotMotor.set_motor_position(index, 180)
    sleep(2)
    position()

def deux():
    position()
    sleep(2)
    RobotMotor.set_motor_position(index, 180)
    RobotMotor.set_motor_position(majeur, 0)
    sleep(2)
    position()

def trois():
    position()
    sleep(2)
    RobotMotor.set_motor_position(pouce_b, 80)
    RobotMotor.set_motor_position(pouce, 180)
    RobotMotor.set_motor_position(index, 180)
    RobotMotor.set_motor_position(majeur, 0)
    sleep(2)
    position()

def quatre():
    position()
    sleep(2)
    RobotMotor.set_motor_position(index, 180)
    RobotMotor.set_motor_position(majeur, 0)
    RobotMotor.set_motor_position(annulaire_auriculaire, 0)
    sleep(2)
    position()
    
def cinq():
    position()
    sleep(2)
    reset_position()
    sleep(2)
    position()

def compter():
    un()
    deux()
    trois()
    quatre()
    cinq()

