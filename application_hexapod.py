import logging

from Service.menu_service import Menu

if __name__ == '__main__':
    logging.basicConfig(filename='logging.log', level=logging.INFO, format='%(asctime)s %(message)s')
    logging.info("Starting application. Saving logs in ~/logging.log")
    menu = Menu()
    menu.starting_menu()
