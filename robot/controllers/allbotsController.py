from robot.robotMotor import RobotMotor
import time

MOTORS = {
    "FRONT_LEFT_ELBOW": RobotMotor(0, 10, 180, 160),
    "FRONT_LEFT_SHOULDER": RobotMotor(1, 10, 135, 110),
    "FRONT_RIGHT_ELBOW": RobotMotor(2, 10, 180, 20),
    "FRONT_RIGHT_SHOULDER": RobotMotor(3, 25, 180, 70),
    "BACK_LEFT_ELBOW": RobotMotor(4, 10, 180, 20),
    "BACK_LEFT_SHOULDER": RobotMotor(5, 25, 180, 110),
    "BACK_RIGHT_ELBOW": RobotMotor(6, 10, 180, 20),
    "BACK_RIGHT_SHOULDER": RobotMotor(7, 10, 135, 50)
}


def set_motor_position(motor_nb: str, angle: str):
    motor_nb, angle = int(motor_nb), int(angle)
    for motor in MOTORS.values():
        if motor.id == motor_nb:
            motor.set_motor_position(angle)
            return


def shift_motor_position(motor_nb: str, angle: str):
    motor_nb, angle = int(motor_nb), int(angle)
    for v in MOTORS.values():
        if v.id == motor_nb:
            v.shift_motor_position(angle)
            return


def reset_position():
    for motor in MOTORS.values():
        motor.reset()
        time.sleep(0.2)


def walk_n_steps(nb_steps: str):
    nb_steps = int(nb_steps)
    for _ in range(nb_steps):
        return
        # TODO: implement walk_n_steps for AllbotsController


def move_backward():
    MOTORS["FRONT_RIGHT_ELBOW"].set_motor_position(50)
    MOTORS["BACK_LEFT_ELBOW"].set_motor_position(50)
    time.sleep(0.2)
    MOTORS["FRONT_RIGHT_SHOULDER"].shift_motor_position(-50)  #
    MOTORS["BACK_LEFT_SHOULDER"].shift_motor_position(50)  #

    time.sleep(0.2)
    MOTORS["FRONT_RIGHT_ELBOW"].set_motor_position(20)
    MOTORS["BACK_LEFT_ELBOW"].set_motor_position(20)
    time.sleep(0.1)
    MOTORS["FRONT_LEFT_ELBOW"].set_motor_position(130)
    MOTORS["BACK_RIGHT_ELBOW"].set_motor_position(50)

    time.sleep(0.1)
    MOTORS["FRONT_RIGHT_SHOULDER"].shift_motor_position(50)  #
    MOTORS["BACK_LEFT_SHOULDER"].shift_motor_position(-50)  #
    time.sleep(0.2)
    # -----------------------------------------------#
    MOTORS["BACK_RIGHT_SHOULDER"].shift_motor_position(-50)  #
    MOTORS["FRONT_LEFT_SHOULDER"].shift_motor_position(50)  #
    time.sleep(0.2)
    MOTORS["FRONT_LEFT_ELBOW"].set_motor_position(160)
    MOTORS["BACK_RIGHT_ELBOW"].set_motor_position(20)
    time.sleep(0.1)
    MOTORS["FRONT_RIGHT_ELBOW"].set_motor_position(50)
    MOTORS["BACK_LEFT_ELBOW"].set_motor_position(50)
    time.sleep(0.1)
    MOTORS["BACK_RIGHT_SHOULDER"].shift_motor_position(50)  #
    MOTORS["FRONT_LEFT_SHOULDER"].shift_motor_position(-50)  #
    time.sleep(0.1)
    MOTORS["FRONT_RIGHT_ELBOW"].set_motor_position(20)
    MOTORS["BACK_LEFT_ELBOW"].set_motor_position(20)
    time.sleep(0.1)
    reset_position()


def do_hi(motor):
    if motor == '0':
        motor = MOTORS["FRONT_LEFT_SHOULDER"]
        other_motor = MOTORS["FRONT_LEFT_ELBOW"]
        reset_position()
        time.sleep(0.5)
        other_motor.set_motor_position(0)
    elif motor == '1':
        motor = MOTORS["FRONT_RIGHT_SHOULDER"]
        other_motor = MOTORS["FRONT_RIGHT_ELBOW"]
        reset_position()
        time.sleep(0.5)
        other_motor.set_motor_position(180)

    for i in range(3):
        motor.shift_motor_position(50)
        time.sleep(0.4)
        motor.shift_motor_position(-50)
        time.sleep(0.4)
    reset_position()


def turn_left():
    MOTORS["FRONT_LEFT_ELBOW"].set_motor_position(120)
    MOTORS["BACK_RIGHT_ELBOW"].set_motor_position(60)
    time.sleep(0.1)
    MOTORS["BACK_RIGHT_SHOULDER"].shift_motor_position(50)  #
    MOTORS["FRONT_LEFT_SHOULDER"].shift_motor_position(50)  #
    time.sleep(0.1)
    MOTORS["FRONT_LEFT_ELBOW"].set_motor_position(160)
    MOTORS["BACK_RIGHT_ELBOW"].set_motor_position(20)

    MOTORS["FRONT_RIGHT_ELBOW"].set_motor_position(60)
    MOTORS["BACK_LEFT_ELBOW"].set_motor_position(60)
    time.sleep(0.1)
    MOTORS["BACK_RIGHT_SHOULDER"].shift_motor_position(-50)  #
    MOTORS["FRONT_LEFT_SHOULDER"].shift_motor_position(-50)  #
    time.sleep(0.1)

    # -------------------------------------#

    time.sleep(0.1)
    MOTORS["FRONT_RIGHT_SHOULDER"].shift_motor_position(50)  #
    MOTORS["BACK_LEFT_SHOULDER"].shift_motor_position(50)  #
    time.sleep(0.1)
    MOTORS["FRONT_RIGHT_ELBOW"].set_motor_position(20)
    MOTORS["BACK_LEFT_ELBOW"].set_motor_position(20)

    MOTORS["FRONT_LEFT_ELBOW"].set_motor_position(120)
    MOTORS["BACK_RIGHT_ELBOW"].set_motor_position(60)
    time.sleep(0.1)
    MOTORS["FRONT_RIGHT_SHOULDER"].shift_motor_position(-50)  #
    MOTORS["BACK_LEFT_SHOULDER"].shift_motor_position(-50)  #
    time.sleep(0.2)
    reset_position()


def turn_right():
    MOTORS["FRONT_LEFT_ELBOW"].set_motor_position(120)
    MOTORS["BACK_RIGHT_ELBOW"].set_motor_position(60)
    time.sleep(0.1)
    MOTORS["BACK_RIGHT_SHOULDER"].shift_motor_position(-50)  #
    MOTORS["FRONT_LEFT_SHOULDER"].shift_motor_position(-50)  #
    time.sleep(0.1)
    MOTORS["FRONT_LEFT_ELBOW"].set_motor_position(160)
    MOTORS["BACK_RIGHT_ELBOW"].set_motor_position(20)

    MOTORS["FRONT_RIGHT_ELBOW"].set_motor_position(60)
    MOTORS["BACK_LEFT_ELBOW"].set_motor_position(60)
    time.sleep(0.1)
    MOTORS["BACK_RIGHT_SHOULDER"].shift_motor_position(50)  #
    MOTORS["FRONT_LEFT_SHOULDER"].shift_motor_position(50)  #
    time.sleep(0.1)

    # -------------------------------------#

    time.sleep(0.1)
    MOTORS["FRONT_RIGHT_SHOULDER"].shift_motor_position(-70)  #
    MOTORS["BACK_LEFT_SHOULDER"].shift_motor_position(-70)  #
    time.sleep(0.1)
    MOTORS["FRONT_RIGHT_ELBOW"].set_motor_position(20)
    MOTORS["BACK_LEFT_ELBOW"].set_motor_position(20)

    MOTORS["FRONT_LEFT_ELBOW"].set_motor_position(120)
    MOTORS["BACK_RIGHT_ELBOW"].set_motor_position(60)
    time.sleep(0.1)
    MOTORS["FRONT_RIGHT_SHOULDER"].shift_motor_position(70)  #
    MOTORS["BACK_LEFT_SHOULDER"].shift_motor_position(70)  #
    time.sleep(0.2)
    reset_position()


def move_forward():
    MOTORS["FRONT_RIGHT_ELBOW"].set_motor_position(50)
    MOTORS["BACK_LEFT_ELBOW"].set_motor_position(50)
    time.sleep(0.2)
    MOTORS["FRONT_RIGHT_SHOULDER"].shift_motor_position(70)
    MOTORS["BACK_LEFT_SHOULDER"].shift_motor_position(-110)

    time.sleep(0.2)
    MOTORS["FRONT_RIGHT_ELBOW"].set_motor_position(20)
    MOTORS["BACK_LEFT_ELBOW"].set_motor_position(20)
    time.sleep(0.1)
    MOTORS["FRONT_LEFT_ELBOW"].set_motor_position(130)
    MOTORS["BACK_RIGHT_ELBOW"].set_motor_position(50)

    time.sleep(0.1)
    MOTORS["FRONT_RIGHT_SHOULDER"].shift_motor_position(-70)
    MOTORS["BACK_LEFT_SHOULDER"].shift_motor_position(110)
    time.sleep(0.2)
    # -----------------------------------------------#
    MOTORS["BACK_RIGHT_SHOULDER"].shift_motor_position(70)
    MOTORS["FRONT_LEFT_SHOULDER"].shift_motor_position(-70)
    time.sleep(0.2)
    MOTORS["FRONT_LEFT_ELBOW"].set_motor_position(160)
    MOTORS["BACK_RIGHT_ELBOW"].set_motor_position(20)
    time.sleep(0.1)
    MOTORS["FRONT_RIGHT_ELBOW"].set_motor_position(50)
    MOTORS["BACK_LEFT_ELBOW"].set_motor_position(50)
    time.sleep(0.1)
    MOTORS["BACK_RIGHT_SHOULDER"].shift_motor_position(-70)
    MOTORS["FRONT_LEFT_SHOULDER"].shift_motor_position(70)
    time.sleep(0.1)
    MOTORS["FRONT_RIGHT_ELBOW"].set_motor_position(20)
    MOTORS["BACK_LEFT_ELBOW"].set_motor_position(20)
    time.sleep(0.1)
    reset_position()
