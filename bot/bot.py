import logging
import os

from bot.planet import Planet
from bot.user import User
from lib.ogame import OGame, BAD_CREDENTIALS, BAD_UNIVERSE_NAME, NOT_LOGGED

from bot import modes
from bot.modes.mode import Mode


class Bot:

    def __init__(self, server_name, user_name, password):
        self.server_name = server_name
        self.user_name = user_name
        self.password = password

        self.session = None
        self.modes = []

        self.user = None
        self.planets = []

    def initialize(self):
        self.user = User(self)
        for planet_id in self.user.get_planet_ids():
            self.planets.append(Planet(self, planet_id))

    def is_logged(self, html=None):
        if not self.session.is_logged(html=html):
            raise NOT_LOGGED
        return True

    def get_url(self, page, params=None):
        return self.session.get_url(page=page, params=params)

    def fetch_eventbox(self):
        return self.session.fetch_eventbox()

    def connect(self):
        try:
            logging.info(f"{self.__class__.__name__}:: Try to login...")
            self.session = OGame(self.server_name, self.user_name, self.password)
            logging.info(f"{self.__class__.__name__}:: Login successful.")
        except BAD_CREDENTIALS:
            logging.error(f"{self.__class__.__name__}:: Please verify your credentials.")
            os._exit(1)
        except BAD_UNIVERSE_NAME:
            logging.error(f"{self.__class__.__name__}:: Please verify your universe name.")
            os._exit(1)
        except AttributeError as e:
            logging.error(f"{self.__class__.__name__}:: Some additional credentials are required ({e}).")
            os._exit(1)

    def active_mode(self, mode_name):
        if any(m.__name__ == mode_name
               for m in Mode.__subclasses__()):
            self.modes.append(getattr(modes, mode_name)(self, self.session))
        else:
            logging.error(f"Cant find {mode_name} mode")
            os._exit(1)
