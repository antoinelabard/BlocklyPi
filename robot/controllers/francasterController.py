import time
from time import sleep
import speech_recognition as sr
from robot.robotMotor import RobotMotor
import robot.speech.francasterSpeech as Speech

MOTORS = {
    "lEFT_ELBOW": RobotMotor(0, 0, 180, 180),
    "LEFT_SHOULDER_ABDUCTOR": RobotMotor(1, 0, 180, 90),
    "LEFT_SHOULDER_ROTATOR": RobotMotor(2, 0, 180, 180),
    "LEFT_SHOULDER_FLEXOR": RobotMotor(3, 0, 180, 90),
    "RIGHT_SHOULDER_FLEXOR": RobotMotor(4, 0, 180, 90),
    "RIGHT_SHOULDER_ABDUCTOR": RobotMotor(5, 0, 180, 0),
    "RIGHT_SHOULDER_ROTATOR": RobotMotor(6, 0, 180, 90),
    "RIGHT_ELBOW": RobotMotor(7, 0, 170, 0),
    "LEFT_HIP": RobotMotor(8, 0, 180, 90),
    "LEFT_KNEE": RobotMotor(9, 0, 135, 0),
    "LEFT_ANKLE": RobotMotor(10, 0, 120, 45),
    "RIGHT_HIP": RobotMotor(11, 0, 180, 90),
    "RIGHT_KNEE": RobotMotor(12, 45, 180, 180),
    "RIGHT_ANKLE": RobotMotor(13, 0, 120, 75),
    "HEAD_YAW": RobotMotor(14, 0, 180, 90),
    "HEAD_PITCH": RobotMotor(15, 35, 140, 90)
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


def set_delay(seconds: str):
    time.sleep(int(seconds))


def walk_n_steps(nb_steps: str):
    nb_steps = int(nb_steps)
    for _ in range(0, nb_steps - 1):
        MOTORS["LEFT_SHOULDER_FLEXOR"].set_motor_position(60)
        sleep(.1)
        MOTORS["RIGHT_SHOULDER_FLEXOR"].set_motor_position(60)
        sleep(.1)
        MOTORS["LEFT_HIP"].set_motor_position(120)
        sleep(.1)
        MOTORS["RIGHT_HIP"].set_motor_position(120)
        sleep(0.5)
        MOTORS["LEFT_SHOULDER_FLEXOR"].set_motor_position(120)
        sleep(.1)
        MOTORS["RIGHT_SHOULDER_FLEXOR"].set_motor_position(120)
        sleep(.1)
        MOTORS["LEFT_HIP"].set_motor_position(60)
        sleep(.1)
        MOTORS["RIGHT_HIP"].set_motor_position(60)
        sleep(.5)


def do_hi(nb_greetings: str):
    """
    :param nb_greetings: the number of times the hand will wave
    """
    nb_greetings = int(nb_greetings)
    MOTORS["RIGHT_SHOULDER_ABDUCTOR"].set_motor_position(130)
    sleep(.1)
    MOTORS["RIGHT_SHOULDER_ROTATOR"].set_motor_position(180)
    sleep(.1)
    for _ in range(nb_greetings):
        MOTORS["RIGHT_ELBOW"].set_motor_position(90)
        sleep(0.5)
        MOTORS["RIGHT_ELBOW"].set_motor_position(0)
        sleep(0.5)


def walk_n_steps_with_knee_lift(nb_steps):
    MOTORS["LEFT_SHOULDER_ROTATOR"].set_motor_position(170)
    MOTORS["RIGHT_SHOULDER_ABDUCTOR"].set_motor_position(10)
    for _ in range(nb_steps):
        MOTORS["LEFT_ELBOW"].set_motor_position(150)
        sleep(0.2)
        MOTORS["LEFT_SHOULDER_FLEXOR"].set_motor_position(90)
        sleep(0.2)
        MOTORS["RIGHT_SHOULDER_FLEXOR"].set_motor_position(60)
        sleep(0.2)
        MOTORS["RIGHT_ELBOW"].set_motor_position(0)
        sleep(0.2)
        MOTORS["LEFT_HIP"].set_motor_position(100)
        sleep(0.2)
        MOTORS["LEFT_KNEE"].set_motor_position(60)
        sleep(0.2)
        MOTORS["RIGHT_HIP"].set_motor_position(120)
        sleep(0.2)
        MOTORS["RIGHT_KNEE"].set_motor_position(180)
        sleep(0.2)
        MOTORS["LEFT_ELBOW"].set_motor_position(180)
        sleep(0.2)
        MOTORS["LEFT_SHOULDER_FLEXOR"].set_motor_position(120)
        sleep(0.2)
        MOTORS["RIGHT_SHOULDER_FLEXOR"].set_motor_position(90)
        sleep(0.2)
        MOTORS["RIGHT_ELBOW"].set_motor_position(30)
        sleep(0.2)
        MOTORS["LEFT_HIP"].set_motor_position(50)
        sleep(0.2)
        MOTORS["LEFT_KNEE"].set_motor_position(0)
        sleep(0.2)
        MOTORS["RIGHT_HIP"].set_motor_position(80)
        sleep(0.2)
        MOTORS["RIGHT_KNEE"].set_motor_position(120)
        sleep(0.2)


def do_no():
    for _ in range(0, 2):
        sleep(.5)
        MOTORS["HEAD_YAW"].set_motor_position(120)
        sleep(.5)
        MOTORS["HEAD_YAW"].set_motor_position(60)


def do_yes():
    for _ in range(0, 2):
        sleep(.5)
        MOTORS["HEAD_PITCH"].set_motor_position(45)
        sleep(.5)
        MOTORS["HEAD_PITCH"].set_motor_position(90)


def speak(text):
    Speech.francaster_speak(text)


def repeat():
    Speech.francaster_repeat()


def answer_to_question(question=""):
    Speech.answer(question)


def record_au():
    r = sr.Recognizer()
    micro = sr.Microphone()
    with micro as source:
        r.adjust_for_ambient_noise(source)
        print("vas-y")
        audio = r.listen(source)
        print("attend")
        voice_data = ''
    try:
        voice_data = r.recognize_google(audio, language="fr-FR")
        print(voice_data)
        if (voice_data == "fais coucou"):
            do_hi(2)
    except sr.UnknownValueError:
        print("Désolé je n'ai pas compris")
    except sr.RequestError:
        print("Une erreur c'est produite")
    return voice_data


def action():
    b = record_au()
    if "fais coucou" in b:
        do_hi(1)
        print("j'ai fait coucou")
        Speech.francaster_speak("j'ai fait coucou", 'fr')
    elif "fais oui" in b:
        do_yes()
        Speech.francaster_speak("j'ai fait oui")
    elif "fais non" in b:
        do_no()
        Speech.francaster_speak("j'ai fait non")
    elif "arrete" in b:
        reset_position()
        exit()
    else:
        exit()


def gifle_g():
    MOTORS["LEFT_ELBOW"].set_motor_position(100)
    sleep(0.3)
    MOTORS["LEFT_SHOULDER_ROTATOR"].set_motor_position(0)
    sleep(0.3)
    MOTORS["LEFT_SHOULDER_FLEXOR"].set_motor_position(0)
    sleep(0.3)
    MOTORS["LEFT_SHOULDER_ROTATOR"].set_motor_position(180)
    sleep(2)
    reset_position()


def leve_le_pied_droit():
    MOTORS["RIGHT_HIP"].set_motor_posion(180)
    MOTORS["RIGHT_KNEE"].set_motor_posion(90)
