import logging
import time

from Domain.Enum.Direction import Direction
from Service.Movement import Movement


class Menu(object):
    movement = None

    def __init__(self):
        logging.info("Init menu service")
        self.movement = Movement()
        # self.movement.rest_position()

    def starting_menu(self):
        print("Choose walking method: \n"
              "1 -> Tripod gait \n"
              "2 -> Crab walk")
        walking_method = input()
        if walking_method.isdecimal():
            self.walking_menu(walking_method)
        else:
            self.starting_menu()

    def walking_menu(self, walking_method):
        while True:
            print("Press w to move forwards or s for backwards")
            user_input = input()
            input_direction = Direction.FORWARD
            if user_input == "w":
                input_direction = Direction.FORWARD
            elif user_input == "s":
                input_direction = Direction.BACKWARD
            self.movement.tripod_gait(direction=input_direction, speed=1)
            time.sleep(1)
        # self.movement.rest_position()
