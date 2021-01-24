import logging
import time

from Domain.Enum.direction import Direction
from Domain.Enum.walking_methode import WalkingMethode
from Service.movement_service import Movement


class Menu(object):
    movement = Movement()

    def __init__(self):
        logging.info("Init menu service")

    def starting_menu(self):
        print("Choose walking method: \n"
              "0 -> Tripod gait \n"
              "1 -> Crab walk")
        walking_method = input()
        if walking_method.isdecimal():
            self.walking_menu(WalkingMethode(walking_method))
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
            self.movement.walking(direction=input_direction, speed=1, walking_method=walking_method)
            time.sleep(1)
        # self.movement.rest_position()
