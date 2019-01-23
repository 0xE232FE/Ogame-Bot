import logging
import random
import time

from lib.ogame.constants import Buildings, Facilities, Research

from bot.modes.mode import Mode


class BuilderOnlyMode(Mode):
    SLEEPING_TIME = 60 * random.randint(2, 25)

    def __init__(self, bot, session):
        super().__init__(bot, session)

    def run(self):
        logging.info(f"{self.__class__.__name__}:: starting...")
        while not self.should_stop:
            logging.info(f"{self.__class__.__name__}:: Checking all planets...")

            for planet_id in self.session.get_planet_ids():
                logging.info(f"{self.__class__.__name__}:: Checking planet {planet_id}...")

                dict_to_build = list(Buildings.values()) + list(Facilities.values()) + list(Research.values())
                for _ in range(1, random.randint(5, 30)):
                    self.session.build(planet_id, random.choice(dict_to_build))
                    time.sleep(random.randint(2, 30))

            time.sleep(self.SLEEPING_TIME)
