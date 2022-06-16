################ Imports #################################
from time import *
from robot.robotMotor import RobotMotor
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

a = RobotMotor(0, 0, 180, 0)
b = RobotMotor(1, 0, 180, 0)
c = RobotMotor(2, 0, 180, 0)
d = RobotMotor(3, 0, 180, 0)

e = RobotMotor(4, 0, 180, 0)
f = RobotMotor(5, 0, 180, 0)
g = RobotMotor(6, 0, 180, 0)
h = RobotMotor(7, 0, 180, 0)  #

i = RobotMotor(8, 0, 180, 0)
j = RobotMotor(9, 0, 180, 0)
k = RobotMotor(10, 0, 180, 0)  #
l = RobotMotor(11, 0, 180, 0)  #

m = RobotMotor(12, 0, 180, 0)
n = RobotMotor(13, 0, 180, 0)
o = RobotMotor(14, 0, 180, 0)
p = RobotMotor(15, 0, 180, 0)

########################################################################

########################################################################

#################  moteurs avec bouton  #####################
    
def moteur_detect(moteur):
    if (moteur == 'a'):
        moteur = a
    elif (moteur == 'b'):
        moteur = b
    elif (moteur == 'c'):
        moteur = c
    elif (moteur == 'd'):
        moteur = d
    elif (moteur == 'e'):
        moteur = e
    elif (moteur == 'f'):
        moteur = f
    elif (moteur == 'g'):
        moteur = g
    elif (moteur == 'h'):
        moteur = h
    elif (moteur == 'i'):
        moteur = i
    elif (moteur == 'j'):
        moteur = j
    elif (moteur == 'k'):
        moteur = k
    elif (moteur == 'l'):
        moteur = l
    elif (moteur == 'm'):
        moteur = m
    elif (moteur == 'n'):
        moteur = n
    elif (moteur == 'o'):
        moteur = o
    elif (moteur == 'p'):
        moteur = p
    return moteur

################################################################################################

########################################################################################""



def plus(moteur, angle:int):  #tourne de 0 a 180 degres +20 +20 en apuiant sur le bouton pousoire
    moteur = moteur_detect(moteur)
    #si egal 0 c'est apuier si non non 
    while (moteur.servo_kit.servo[moteur.id].angle != 180):
        etat = GPIO.input(bouton_pin)
        
        if (etat == 0) :
            print(etat)
            RobotMotor.shift_motor_position(moteur, angle)
                    
        sleep(0.1)
    


def moins(moteur, angle:int):  #tourne de 180 a 0 degres  -20 -20 en apuiant sur le bouton pousoire
    moteur = moteur_detect(moteur)
    while (moteur.servo_kit.servo[moteur.id].angle >= 0):
        etat = GPIO.input(bouton_pin)
            
        if (etat == 0):
            print(etat)
            RobotMotor.shift_motor_position(moteur, -angle)
        
        sleep(0.1)
   
        
def tourne(moteur, angle:int): # si <180 augmente si non degrade
    moteur = moteur_detect(moteur)
    while True:
        if(moteur.servo_kit.servo[moteur.id].angle <= 180):
            plus(moteur, angle)
        if(moteur.servo_kit.servo[moteur.id].angle >= 180):
            moins(moteur, angle)


def position(moteur, angle:int):# positionner un moteur a un angle
    moteur = moteur_detect(moteur)     
    RobotMotor.set_motor_position(moteur, angle)
            
            
###############################################################################           
            
#########     LED      #########################################################
    
            
def led_bouton():   #allume la led avec bouton pousoire
    while True:
        etat = GPIO.input(bouton_pin)

        # etat==0 => bouton appuye => LED allumee
        if (etat == 0) :
            print("Appui detecte")
            GPIO.output(led_pin,True)

        else :
            GPIO.output(led_pin, False)

        # Temps de repos pour eviter la surchauffe du processeur
        sleep(0.2)
        
     
        
def led_b():
    etat_b = GPIO.input(bouton_pin)
    if (etat_b == 1) :
        while(etat_b == 1):
            etat_b = GPIO.input(bouton_pin)
            sleep(0.1)
        if (etat_b == 0):
            if(etat_l == 0):
                GPIO.output(led_pin,True)
                etat_l = 1
            else:
                GPIO.output(led_pin,False)
                etat_l = 0

        
       
        
def led_on():   #allumer la led
    GPIO.output(led_pin,True)
        
        
def led_off():  #eteindre la led
    GPIO.output(led_pin,False)
        
        
def led_clignote(rep,temps): #clignoter la led avec un interval de temps temps
    while (rep):
        GPIO.output(led_pin,True)
        sleep(temps)
        GPIO.output(led_pin,False)
        sleep(temps)
        rep = rep - 1



def led_clignote_bouton(rep,temps):  #clignoter la led avec un interval de temps temps avec bouton
    etat = GPIO.input(bouton_pin)     
        
    while (etat == 1) :
        GPIO.output(led_pin,False)
        etat = GPIO.input(bouton_pin)
        
    if (etat == 0) :
        led_clignote(rep,temps) 

#######################################################################

#########################  bouton   ####################################


def bouton():
    etat = GPIO.input(bouton_pin)
    a = False
    while (etat == 1) :
        sleep(0.1)
        etat = GPIO.input(bouton_pin)
        
    if(etat == 0):
        a = True
    return a
    
def excute():
    b = bouton()
    return b
    
########################################################################
##############  sleep  ##################################

def repos(temps):
    if (temps == 'a'):
        temps = 0.1
    elif (temps == 'b'):
        temps = 0.2
    elif (temps == 'c'):
        temps = 0.5
    elif (temps == 'd'):
        temps = 1
    elif (temps == 'e'):
        temps = 2
    sleep(temps)

    