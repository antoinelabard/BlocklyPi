################ Imports #################################
from time import *
from robot.robotMotor import RobotMotor

# set of constants used to replace the motor numbers by more meaningful names

pouce_b = RobotMotor(0, 0, 130, 80)
pouce = RobotMotor(1, 50, 180, 180)
index = RobotMotor(2, 0, 180, 180)
majeur = RobotMotor(3, 0, 160, 0)
annulaire_auriculaire = RobotMotor(4, 0, 180, 0)
main = RobotMotor(5, 0, 180, 90)

 

########################################################################

########### fonctions du bras robot #####################





def reset_position():
    RobotMotor.set_motor_position(pouce_b, 80)
    RobotMotor.set_motor_position(pouce, 180)
    RobotMotor.set_motor_position(index, 180)
    RobotMotor.set_motor_position(majeur, 0)
    RobotMotor.set_motor_position(annulaire_auriculaire, 0)
    RobotMotor.set_motor_position(main, 90)
       
def position():
    RobotMotor.set_motor_position(pouce_b, 0)
    RobotMotor.set_motor_position(pouce, 50)
    RobotMotor.set_motor_position(index, 0)
    RobotMotor.set_motor_position(majeur, 160)
    RobotMotor.set_motor_position(annulaire_auriculaire, 180)
    RobotMotor.set_motor_position(main, 0)


def main():
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

