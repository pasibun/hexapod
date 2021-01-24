import logging
import time

import busio
from adafruit_pca9685 import PCA9685
from adafruit_servokit import ServoKit
from board import SCL, SDA

from Domain.Enum.direction import Direction
from Domain.Hexa import Hexa


class Movement(object):
    servo_board_1 = ServoKit(channels=16, address=0x40)
    servo_board_2 = ServoKit(channels=16, address=0x41)
    hexapod = Hexa()

    # Create the I2C bus interface.
    i2c_bus = busio.I2C(SCL, SDA)
    pca = PCA9685(i2c_bus)
    pca.frequency = 60

    max_step_size = 50

    def __init__(self):
        logging.info("Init movement service")

    def tripod_gait(self, direction, speed):
        direction_left = direction
        direction_right = self.determine_direction(direction)
        for i in range(2):
            self.move_tripod_gait(self.hexapod.tripod_gait_right, direction_right, speed)
            time.sleep(0.3)
            self.move_tripod_gait(self.hexapod.tripod_gait_left, direction_left, speed)

            direction_left = self.determine_direction(direction_left)
            direction_right = self.determine_direction(direction_right)
            time.sleep(1)

    def move_tripod_gait(self, legs, direction, speed):
        logging.info("Staring to walk with speed: " + str(speed) + ", direction:" + str(direction))
        try:
            for leg in legs:
                logging.info("moving leg: " + str(leg.name))
                angle = self.determine_angle(leg, direction)
                if leg.tibia < 15:
                    self.servo_board_1.servo[leg.coxa].angle = angle
                else:
                    self.servo_board_2.servo[leg.coxa - 15].angle = angle
        except:
            logging.error("Bende is kapot in move_tripod_gait")

    def determine_angle(self, leg, direction):
        angle = leg.max_front_position[0]
        if direction == Direction.BACKWARD:
            angle = leg.max_back_position[0]
        return angle

    def determine_direction(self, direction):
        if direction == Direction.BACKWARD:
            return Direction.FORWARD
        else:
            return Direction.BACKWARD
    # def rest_position(self):
    #     logging.info("Putting Hexapod in rest position")
    #     for position in Hexa.reset_position:
    #         servo = position[0]
    #         angle = position[1]
    #         if servo > 14:
    #             if servo == 15:
    #                 servo = 0
    #             if servo == 16:
    #                 servo = 1
    #             if servo == 17:
    #                 servo = 2
    #             self.servo_board_2.servo[servo].angle = angle
    #         else:
    #             self.servo_board_1.servo[servo].angle = angle

    # def tripod_gait_oud(self, direction, step_size, speed):
    #     logging.info("Staring to walk with step size: " + str(step_size) + ", speed: " + str(speed) + ", direction:" + str(direction))
    #     try:
    #         walking_position = Hexa.reset_position
    #         for first in walking_position:
    #             servo = first[0]
    #             angle = first[1]
    #             if servo == 0 or servo == 6 or servo == 12:
    #                 new_angle = self.determine_angle(angle, Hexa.reset_position[servo], direction, step_size)
    #                 walking_position[servo][1] = new_angle
    #                 self.servo_board_1.servo[servo].angle = angle
    #                 time.sleep(speed)
    #
    #         for second in walking_position:
    #             servo = second[0]
    #             angle = second[1]
    #             if servo == 3 or servo == 9 or servo == 15:
    #                 new_angle = self.determine_angle(angle, Hexa.reset_position[servo], direction, step_size)
    #                 walking_position[servo][1] = new_angle
    #                 if servo == 15:
    #                     self.servo_board_2.servo[servo].angle = angle
    #                 else:
    #                     self.servo_board_1.servo[servo].angle = angle
    #                 time.sleep(speed)
    #     except:
    #         logging.error("Something went wrong with walking.")
    #
    # def determine_angle(self, angle, reset_angle, direction, step_size):
    #     try:
    #         if step_size > self.max_step_size:
    #             step_size = self.max_step_size
    #
    #         if direction == Direction.FORWARD:
    #             print(angle)
    #             print(reset_angle)
    #             print(angle + step_size)
    #             if angle == reset_angle:
    #                 print(reset_angle - step_size)
    #                 new_angle = reset_angle - step_size
    #             elif angle + step_size == reset_angle:
    #                 print(reset_angle + step_size)
    #                 new_angle = reset_angle + step_size
    #             else:
    #                 new_angle = reset_angle - step_size
    #         elif direction == Direction.BACKWARD:
    #             if angle == reset_angle:
    #                 new_angle = reset_angle + step_size
    #             elif angle + step_size == reset_angle:
    #                 new_angle = reset_angle + step_size
    #             else:
    #                 new_angle = reset_angle - step_size
    #         else:
    #             new_angle = reset_angle
    #     except:
    #         logging.error("Something went wrong with determine_angle.")
    #         new_angle = reset_angle
    #     logging.info("Old angle: " + angle + ". New angle: " + new_angle)
    #     return new_angle