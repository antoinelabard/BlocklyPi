from time import *
from robot.robotMotor import RobotMotor
import RPi.GPIO as GPIO
import board
import busio
import adafruit_ads1x15.ads1115 as ADS  # importer le module pour la carte ads1115
from adafruit_ads1x15.analog_in import AnalogIn

#####  definition des pins#####
led_pin = 23
bouton_pin = 24

etat_l = 0

GPIO.setmode(GPIO.BCM)

# Definition des pins en entree / sortie
GPIO.setup(bouton_pin, GPIO.IN, pull_up_down=GPIO.PUD_UP)
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
    if moteur == 'a':
        moteur = a
    elif moteur == 'b':
        moteur = b
    elif moteur == 'c':
        moteur = c
    elif moteur == 'd':
        moteur = d
    elif moteur == 'e':
        moteur = e
    elif moteur == 'f':
        moteur = f
    elif moteur == 'g':
        moteur = g
    elif moteur == 'h':
        moteur = h
    elif moteur == 'i':
        moteur = i
    elif moteur == 'j':
        moteur = j
    elif moteur == 'k':
        moteur = k
    elif moteur == 'l':
        moteur = l
    elif moteur == 'm':
        moteur = m
    elif moteur == 'n':
        moteur = n
    elif moteur == 'o':
        moteur = o
    elif moteur == 'p':
        moteur = p
    return moteur


################################################################################################

########################################################################################""


def plus(moteur, angle: int):  # tourne de 0 a 180 degres +20 +20 en apuiant sur le bouton pousoire
    moteur = moteur_detect(moteur)
    # si egal 0 c'est apuier si 1 non appuier
    while moteur.servo_kit.servo[moteur.id].angle != 180:
        etat = GPIO.input(bouton_pin)

        if etat == 0:
            print(etat)
            RobotMotor.shift_motor_position(moteur, angle)

        sleep(0.1)


def moins(moteur, angle: int):  # tourne de 180 a 0 degres  -20 -20 en apuiant sur le bouton pousoire
    moteur = moteur_detect(moteur)
    while moteur.servo_kit.servo[moteur.id].angle >= 0:
        etat = GPIO.input(bouton_pin)

        if etat == 0:
            print(etat)
            RobotMotor.shift_motor_position(moteur, -angle)

        sleep(0.1)


def tourne(moteur, angle: int):  # si <180 augmente si non degrade
    moteur = moteur_detect(moteur)
    while True:
        if moteur.servo_kit.servo[moteur.id].angle <= 180:
            plus(moteur, angle)
        if moteur.servo_kit.servo[moteur.id].angle >= 180:
            moins(moteur, angle)


def position(moteur, angle: int):  # positionner un moteur a un angle
    moteur = moteur_detect(moteur)
    RobotMotor.set_motor_position(moteur, angle)


###############################################################################           

#########     LED      #########################################################


def led_bouton():  # allume la led avec bouton pousoire
    while True:
        etat = GPIO.input(bouton_pin)

        # etat==0 => bouton appuye => LED allumee
        if etat == 0:
            print("Appui detecte")
            GPIO.output(led_pin, True)

        else:
            GPIO.output(led_pin, False)

        # Temps de repos pour eviter la surchauffe du processeur
        sleep(0.2)


def led_b():
    etat_b = GPIO.input(bouton_pin)
    if etat_b == 1:
        while etat_b == 1:
            etat_b = GPIO.input(bouton_pin)
            sleep(0.1)
        if etat_b == 0:
            if etat_l == 0:
                GPIO.output(led_pin, True)
                etat_l = 1
            else:
                GPIO.output(led_pin, False)
                etat_l = 0


def led_on():  # allumer la led
    GPIO.output(led_pin, True)


def led_off():  # eteindre la led
    GPIO.output(led_pin, False)


def led_clignote(rep, temps):  # clignoter la led avec un interval de temps temps
    while rep:
        GPIO.output(led_pin, True)
        sleep(temps)
        GPIO.output(led_pin, False)
        sleep(temps)
        rep = rep - 1


def led_clignote_bouton(rep, temps):  # clignoter la led avec un interval de temps temps avec bouton
    etat = GPIO.input(bouton_pin)

    while etat == 1:
        GPIO.output(led_pin, False)
        etat = GPIO.input(bouton_pin)

    if etat == 0:
        led_clignote(rep, temps)

    #######################################################################


#########################  bouton   ####################################

def bouton():
    etat = GPIO.input(bouton_pin)
    if etat == 1:
        a = False
    else:
        a = True
    return a


########################################################################
##############  sleep  ##################################

def repos(temps):
    if temps == 'a':
        temps = 0.1
        sleep(temps)
    elif temps == 'b':
        temps = 0.2
        sleep(temps)
    elif temps == 'c':
        temps = 0.5
        sleep(temps)
    elif temps == 'd':
        temps = 1
        sleep(temps)
    elif temps == 'e':
        temps = 2
        sleep(temps)


#################################################################################################"
######################## convertisseur analogique/numerique   et potensiometre ##########################


i2c = busio.I2C(board.SCL, board.SDA)  # initialiser le bus i2c

# creer l'objet ads
ads = ADS.ADS1115(i2c)

# creer le canal d'entrer du signal analogique
chan = AnalogIn(ads, ADS.P0)  # mode asymetrique
# print(chan.value, chan.voltage)

chan2 = AnalogIn(ads, ADS.P0, ADS.P1)  # mode differentiel


def pourcentage_potentiometre():
    val_max = 32767  # la valeur max lu par l'ADC

    pourcentage_de_tenssion = chan.value * 100 / val_max  # calculer le pourcentage de la tension reduite par le potentiometre

    print(pourcentage_de_tenssion)
    return pourcentage_de_tenssion


###### mettre le moteur le moteur a la position indiquer par le potentiometre#####

def moteur_potentiometre(moteur):
    moteur = moteur_detect(moteur)
    x = pourcentage_potentiometre() * 180 / 100  # l'angle calculer a partire du pourcetange du potentiometre

    RobotMotor.set_motor_position(moteur, x)
    sleep(0.2)


#################################################ultara son ###################"""


Trig = 27  # Entree Trig du HC-SR04 branchee au GPIO 23
Echo = 22  # Sortie Echo du HC-SR04 branchee au GPIO 24

GPIO.setup(Trig, GPIO.OUT)
GPIO.setup(Echo, GPIO.IN)

GPIO.output(Trig, False)



def distance():
    GPIO.output(Trig, True)
    sleep(0.00001)
    GPIO.output(Trig, False)

    while GPIO.input(Echo) == 0:  ## Emission de l'ultrason
        debutImpulsion = time()

    while GPIO.input(Echo) == 1:  ## Retour de l'Echo
        finImpulsion = time()

    ## Vitesse du son = 340 m/s  #arndi a 1 chiffre apres la virgule
    distance = round((finImpulsion - debutImpulsion) * 340 * 100 / 2, 1)

    print("La distance est de : ", distance, " cm")

    GPIO.cleanup()
