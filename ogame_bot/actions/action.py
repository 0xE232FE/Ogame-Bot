import logging
import random
import threading
import time
from abc import ABCMeta, abstractmethod


class Action(threading.Thread):
    __metaclass__ = ABCMeta

    SLEEPING_TIME_FACTOR = 30
    SLEEPING_TIME_MIN = 5
    SLEEPING_TIME_MAX = 25

    def __init__(self, bot, mode):
        super().__init__()
        self.bot = bot
        self.mode = mode
        self.evaluation = 0

    def run(self):
        while True:
            for planet in self.bot.planets:
                logging.info(f"{self.__class__.__name__}:: on planet {planet.planet_id}...")
                self.perform_action(planet)
                time.sleep(random.random(self.SLEEPING_TIME_MIN, self.SLEEPING_TIME_MAX))
            time.sleep(self.SLEEPING_TIME_FACTOR * random.random(self.SLEEPING_TIME_MIN, self.SLEEPING_TIME_MAX))

    @abstractmethod
    def perform_action(self, planet):
        raise NotImplemented("perform_action not implemented.")
