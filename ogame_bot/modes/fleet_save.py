import logging
import random
import time

from ogame_bot.modes.mode import Mode


class FleetSaveMode(Mode):
    SLEEPING_TIME_FACTOR = 10

    def __init__(self, bot, session):
        super().__init__(bot, session)

    def run(self):
        logging.info(f"{self.__class__.__name__}:: starting...")
        while not self.should_stop:
            if self.bot.user.is_under_attack():
                logging.warning(f"{self.__class__.__name__}:: Is under attack !!")

            time.sleep(self.SLEEPING_TIME_FACTOR * random.randint(6, 18))
