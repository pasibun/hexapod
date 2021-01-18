import logging
import time

from Domain.Direction import Direction
from Service.Movement import Movement


class Menu(object):
    movement = None

    def __init__(self):
        logging.info("Init menu service")
        self.movement = Movement()
        self.movement.rest_position()

    def starting_menu(self):
        print("Choose walking method: \n"
              "1 -> Tripod gait \n"
              "2 -> Crab walk")
        walking_method = input()
        if walking_method.isdecimal():
            self.walking_menu()
        else:
            self.starting_menu()

    def walking_menu(self):
        print("Press w to move forwards or s for backwards")
        user_input = input()
        input_direction = Direction.FORWARD
        if user_input == "w":
            input_direction = Direction.FORWARD
        elif user_input == "s":
            input_direction = Direction.BACKWARD
        self.movement.tripod_gait(input_direction, 25, 0.5)
        time.sleep(1)
        self.movement.rest_position()
