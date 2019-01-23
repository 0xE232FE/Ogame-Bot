import logging

from ogame import OGame

from bot import modes
from bot.modes.mode import Mode


class Bot:

    def __init__(self, server_name, user_name, password):
        self.server_name = server_name
        self.user_name = user_name
        self.password = password

        self.session = None
        self.modes = []

    def connect(self):
        logging.info(f"{self.__class__.__name__}:: Try to login...")
        self.session = OGame(self.server_name, self.user_name, self.password)
        logging.info(f"{self.__class__.__name__}:: Login successful.")

    def active_mode(self, mode_name):
        if any(m.__name__ == mode_name
               for m in Mode.__subclasses__()):
            self.modes.append(getattr(modes, mode_name)(self, self.session))
        else:
            logging.error(f"Cant find {mode_name} mode")
