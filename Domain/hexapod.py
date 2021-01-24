import logging

from Domain.Enum.leg_name import LegName
from Domain.hexapod_leg import HexapodLeg


class Hexapod(object):
    front_right = None
    middle_right = None
    back_right = None
    front_left = None
    middle_left = None
    back_left = None

    tripod_gait_right = None
    tripod_gait_left = None

    def __init__(self):
        logging.info("Init Hexa")
        self.front_left = HexapodLeg(name=LegName.FRONT_LEFT, coxa=0, femur=1, tibia=2, front=[150], back=[25], left=[], right=[], rest=[100])
        self.middle_left = HexapodLeg(name=LegName.MIDDLE_LEFT, coxa=3, femur=4, tibia=5, front=[125], back=[40], left=[], right=[], rest=[90])
        self.back_left = HexapodLeg(name=LegName.BACK_LEFT, coxa=6, femur=7, tibia=8, front=[125], back=[30], left=[], right=[], rest=[80])
        self.front_right = HexapodLeg(name=LegName.FRONT_RIGHT, coxa=9, femur=10, tibia=11, front=[30], back=[130], left=[], right=[], rest=[70])
        self.middle_right = HexapodLeg(name=LegName.MIDDLE_RIGHT, coxa=12, femur=13, tibia=14, front=[50], back=[140], left=[], right=[], rest=[95])
        self.back_right = HexapodLeg(name=LegName.BACK_RIGHT, coxa=15, femur=16, tibia=17, front=[40], back=[140], left=[], right=[], rest=[100])

        self.tripod_gait_right = [self.front_right, self.back_right, self.middle_left]
        self.tripod_gait_left = [self.front_left, self.back_left, self.middle_right]
