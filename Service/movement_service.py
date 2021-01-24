import logging

import busio
from adafruit_pca9685 import PCA9685
from adafruit_servokit import ServoKit
from board import SCL, SDA

from Domain.Enum.walking_methode import WalkingMethode
from Domain.hexapod import Hexapod
from Helper.tripod_gait import TripodGait


class Movement(object):
    servo_board_1 = ServoKit(channels=16, address=0x40)
    servo_board_2 = ServoKit(channels=16, address=0x41)
    hexapod = Hexapod()

    # Create the I2C bus interface.
    i2c_bus = busio.I2C(SCL, SDA)
    pca = PCA9685(i2c_bus)
    pca.frequency = 60

    max_step_size = 50

    def __init__(self):
        logging.info("Init movement service")

    def walking(self, direction, speed, walking_method):
        if walking_method == WalkingMethode.TRIPOD_GAIT:
            TripodGait().walk(direction=direction, speed=speed, hexapod=self.hexapod, servo_board_1=self.servo_board_1, servo_board_2=self.servo_board_2)

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
