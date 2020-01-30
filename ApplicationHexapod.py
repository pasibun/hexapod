import logging
import sys
import termios
import time
import tty

from Direction import Direction
from Movement import Movement
from PlaystationController import PlaystationController


def getch():
    fd = sys.stdin.fileno()
    old_settings = termios.tcgetattr(fd)
    try:
        tty.setraw(sys.stdin.fileno())
        ch = sys.stdin.read(1)
    finally:
        termios.tcsetattr(fd, termios.TCSADRAIN, old_settings)
    return ch


if __name__ == '__main__':
    logging.basicConfig(filename='logging.log', level=logging.INFO, format='%(asctime)s %(message)s')
    logging.info("Starting application")
    movement = Movement()
    ps3 = PlaystationController()
    movement.rest_position()
    print("Saving logs in ~/logging.log")
    ps3.getInformation()
    while True:
        print("Press w to move forwards or s for backwards")
        user_input = getch()
        input_direction = Direction.FORWARD
        if user_input == "w":
            input_direction = Direction.FORWARD
        elif user_input == "s":
            input_direction = Direction.BACKWARD
        movement.walking(input_direction, 25, 0.05)
        time.sleep(1)
        movement.rest_position()
