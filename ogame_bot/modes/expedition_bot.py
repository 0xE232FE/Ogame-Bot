import logging
import random
import time

from ogame_bot.modes.mode import Mode


class ExpeditionBotMode(Mode):
    SLEEPING_TIME_FACTOR = 60

    def __init__(self, bot, session):
        super().__init__(bot, session)

    def run(self):
        logging.info(f"{self.__class__.__name__}:: starting...")
        while not self.should_stop:
            logging.info(f"{self.__class__.__name__}:: Checking all planets...")

            for planet in self.bot.planets:
                logging.info(f"{self.__class__.__name__}:: Checking planet {planet.planet_id}...")

            time.sleep(self.SLEEPING_TIME_FACTOR * random.randint(1, 10))
