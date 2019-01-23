import logging
import time

from ogame.constants import Buildings

from bot.modes.mode import Mode


class BuilderOnlyMode(Mode):
    SLEEPING_TIME = 120

    def __init__(self, bot, session):
        super().__init__(bot, session)

    def run(self):
        logging.info(f"{self.__class__.__name__}:: starting...")
        while not self.should_stop:
            logging.info(f"{self.__class__.__name__}:: Checking all planets...")

            for planet_id in self.session.get_planet_ids():
                logging.info(f"{self.__class__.__name__}:: Checking planet {planet_id}...")

                for building in Buildings:
                    print(building)
                    # self.session.build(planet_id, building)

            time.sleep(self.SLEEPING_TIME)
