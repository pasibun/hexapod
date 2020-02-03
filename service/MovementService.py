import logging

import busio
from adafruit_pca9685 import PCA9685
from adafruit_servokit import ServoKit
from board import SCL, SDA

from helper.NormalWalkHelper import NormalWalkHelper
from model.Hexa import Hexa


class MovementService(object):
    servo_board_1 = ServoKit(channels=16, address=0x40)
    servo_board_2 = ServoKit(channels=16, address=0x41)

    # Create the I2C bus interface.
    i2c_bus = busio.I2C(SCL, SDA)
    pca = PCA9685(i2c_bus)
    pca.frequency = 50

    hexapod = Hexa()
    walkhelper = NormalWalkHelper()
    first_time = True

    def rest_position(self):
        logging.info("Putting Hexapod in rest position")
        for position in self.hexapod.reset_position:
            servo = position[0]
            angle = position[1]
            if servo > 14:
                if servo == 15:
                    servo = 0
                if servo == 16:
                    servo = 1
                if servo == 17:
                    servo = 2
                self.servo_board_2.servo[servo].angle = angle
            else:
                self.servo_board_1.servo[servo].angle = angle

    def walking(self, direction, step_size, speed):
        global first_time
        logging.info(
            "Staring to walk with step size: " + str(step_size) + ", speed: " + str(speed) + ", direction: " + str(
                direction))
        try:
            for start_legs in self.hexapod.current_position:
                servo = start_legs[0]
                if servo in [0, 1, 2, 6, 7, 8, 12, 13, 14]:
                    new_angle = self.walkhelper.move_start_legs(servo, direction, step_size)
                    self.servo_board_1.servo[servo].angle = new_angle
            if not self.first_time:
                for second_legs in self.hexapod.current_position:
                    servo = second_legs[0]
                    if servo in [3, 4, 5, 9, 10, 11, 15, 16, 17]:
                        new_angle = self.walkhelper.start_second_legs(servo, direction, step_size)
                        if servo in [15, 16, 17]:
                            self.servo_board_2.servo[servo].angle = new_angle
                        else:
                            self.servo_board_1.servo[servo].angle = new_angle
            else:
                self.first_time = False
        except:
            logging.error("Something went wrong with walking.")
