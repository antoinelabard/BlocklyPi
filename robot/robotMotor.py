from adafruit_servokit import ServoKit


class RobotMotor:
    """
    RobotController stores all the data relative to a motor.
    """

    # the number of the connector on which the motor is connected on the card
    id: int

    min_angle: int
    max_angle: int

    initial_angle: int

    # constants used for the is_in_range function
    IN_RANGE = 0
    BELOW_RANGE = -1
    ABOVE_RANGE = 1

    servo_kit = ServoKit(channels=16)

    def __init__(self, id: int, min_angle: int, max_angle: int, initial_angle: int):
        self.id = id
        self.min_angle = min_angle
        self.max_angle = max_angle
        self.initial_angle = initial_angle

    def is_in_range(self, angle: int):
        """
        @:param
            - angle: the set-point angle.
        @:return
            - IN_RANGE if angle is within the value provided by angle is between the values provided by range.
            - BELOW_RANGE if it is below the minimum value.
            - ABOVE_RANGE if it is above the maximum value.
        """
        if self.min_angle <= angle <= self.max_angle:
            return self.IN_RANGE
        elif self.min_angle > angle:
            return self.BELOW_RANGE
        else:
            return self.ABOVE_RANGE

    def set_motor_position(self, angle: int):
        in_range = self.is_in_range(angle)
        if in_range == 0:
            self.servo_kit.servo[self.id].angle = angle
        elif in_range == -1:
            self.servo_kit.servo[self.id].angle = self.min_angle
        elif in_range == 1:
            self.servo_kit.servo[self.id].angle = self.max_angle

    def shift_motor_position(self, angle: int):
        shifted_angle = self.servo_kit.servo[self.id].angle + angle
        in_range = self.is_in_range(shifted_angle)
        if in_range == 0:
            self.servo_kit.servo[self.id].angle += angle
        elif in_range == -1:
            self.servo_kit.servo[self.id].angle = self.min_angle
        elif in_range == 1:
            self.servo_kit.servo[self.id].angle = self.max_angle

    def reset(self):
        self.set_motor_position(self.initial_angle)
