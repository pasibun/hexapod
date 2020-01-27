import logging
import time

from Direction import Direction
from Movement import Movement

if __name__ == '__main__':
    logging.basicConfig(filename='logging.log', level=logging.INFO, format='%(asctime)s %(message)s')
    logging.info("Starting application")
    movement = Movement()
    movement.rest_position()
    print("Saving logs in ~/logging.log")
    while True:
        print("Press w to move forwards or s for backwards")
        user_input = input()
        input_direction = Direction.FORWARD
        if user_input == "w":
            input_direction = Direction.FORWARD
        elif user_input == "s":
            input_direction = Direction.BACKWARD
        movement.walking(input_direction, 50, 0.1)
        time.sleep(1)
        movement.rest_position()
