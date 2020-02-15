import logging
import time

from model.Direction import Direction
from model.Hexa import Hexa


class NormalWalkHelper(object):
    hexapod = Hexa()

    def move_start_legs(self, servo, direction, step_size):
        side = self.determin_side(servo)
        if servo in [0, 6, 12]:
            return self.move_cova(servo, side, direction, step_size)
        if servo in [1, 7, 13]:
            time.sleep(0.1)
            return self.move_femur(servo, side)

    def start_second_legs(self, servo, direction, step_size):
        side = self.determin_side(servo)
        if servo in [3, 9, 15]:
            return self.move_cova(servo, side, direction, step_size)
        if servo in [4, 10, 16]:
            time.sleep(0.1)
            return self.move_femur(servo, side)

    def move_cova(self, servo, side, direction, step_size):
        current_angle_coxa = self.hexapod.current_position[servo][1]
        reset_angle_coxa = self.hexapod.reset_position[servo]
        new_angle_coxa = self.determine_coxa_angle(current_angle_coxa, reset_angle_coxa[1], direction, step_size, side)

        logging.info("Moving coxa. Old angle: " + str(self.hexapod.current_position[servo][1]) + "New angle: " + str(
            new_angle_coxa))
        self.hexapod.current_position[servo][1] = new_angle_coxa
        return new_angle_coxa

    def move_femur(self, servo, side):
        reset_angle_femur = self.hexapod.reset_position[servo]
        femur_step = self.hexapod.default_step_size_femur

        # Bepalen waar de coxa staat.
        coxa_angle = self.hexapod.current_position[servo - 1][1]
        reset_angle_coxa = self.hexapod.reset_position[servo - 1]
        if (side == "R" and coxa_angle > reset_angle_coxa[1]) or (side == "L" and coxa_angle < reset_angle_coxa[1]):
            new_femur_angle = reset_angle_femur[1] - femur_step
        else:
            new_femur_angle = reset_angle_femur[1]

        logging.info("Moving femur. Old angle: " + str(self.hexapod.current_position[servo][1]) + "New angle: " + str(
            new_femur_angle))
        self.hexapod.current_position[servo][1] = new_femur_angle
        return new_femur_angle

    def determine_coxa_angle(self, angle, reset_angle, direction, step_size, side):
        try:
            new_angle = reset_angle
            if direction == Direction.FORWARD:
                if angle == reset_angle:
                    if side == "R":
                        new_angle = reset_angle + step_size
                    else:
                        new_angle = reset_angle - step_size
                elif angle - step_size == reset_angle:
                    new_angle = reset_angle - step_size
                else:
                    new_angle = reset_angle + step_size
        except:
            logging.error("Something went wrong with determine_angle.")
            new_angle = reset_angle
        return new_angle

    def determin_side(self, servo):
        if servo in [0, 1, 2, 3, 4, 5, 6, 7, 8]:
            return "R"
        else:
            return "L"
