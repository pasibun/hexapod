import logging
import time

from Domain.Enum.direction import Direction


class TripodGait(object):

    def __init__(self):
        logging.info("init tripod gait")

    def walk(self, direction, speed, hexapod, servo_board_1, servo_board_2):
        direction_left = direction
        direction_right = self.determine_direction(direction)
        for i in range(2):
            self.move_tripod_gait(hexapod.tripod_gait_right, direction_right, speed, servo_board_1, servo_board_2)
            time.sleep(0.3)
            self.move_tripod_gait(hexapod.tripod_gait_left, direction_left, speed, servo_board_1, servo_board_2)

            direction_left = self.determine_direction(direction_left)
            direction_right = self.determine_direction(direction_right)
            time.sleep(1)

    def move_tripod_gait(self, legs, direction, speed, servo_board_1, servo_board_2):
        logging.info("Staring to walk with speed: " + str(speed) + ", direction:" + str(direction))
        try:
            for leg in legs:
                logging.info("moving leg: " + str(leg.name))
                angle = self.determine_angle(leg, direction)
                if leg.tibia < 15:
                    servo_board_1.servo[leg.coxa].angle = angle
                else:
                    servo_board_2.servo[leg.coxa - 15].angle = angle
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
