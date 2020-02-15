import logging
import sys
import termios
import time
import tty
import os

from model.Direction import Direction
from service.MovementService import MovementService
from service.PlaystationService import PlaystationService


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
    try:
        logging.basicConfig(filename='logging.log', level=logging.INFO, format='%(asctime)s %(message)s')
        logging.info("Starting application")
        movement = MovementService()
        #ps3 = PlaystationService()
        movement.rest_position()
        print("Saving logs in ~/logging.log")
        #ps3.getInformation()
        while True:
            print("Press w to move forwards or s for backwards")
            user_input = input()  #getch()
            input_direction = Direction.FORWARD
            if user_input == "w":
                input_direction = Direction.FORWARD
            elif user_input == "s":
                input_direction = Direction.BACKWARD
            print("Hoe vaak moet die bewegen?")
            hoevaak = input()
            for i in range(int(hoevaak)):
                movement.walking(input_direction, 25, 0.01)
            time.sleep(1)

    except KeyboardInterrupt:
        print("Exiting program.")
        logging.error("Exit application")
        os.system("stty echo")
