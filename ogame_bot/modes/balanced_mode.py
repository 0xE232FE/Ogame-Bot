import logging
import random
import time

from ogame_bot.actions.fleet_manager import FleetManager
from ogame_bot.actions.attacker import Attacker
from ogame_bot.actions.economy import Economy
from ogame_bot.actions.researcher import Researcher
from ogame_bot.modes.mode import Mode


class BalancedMode(Mode):
    SLEEPING_TIME_FACTOR = 60

    def __init__(self, bot, session):
        super().__init__(bot, session)
        self.action_matrix = None

    def run(self):
        logging.info(f"{self.__class__.__name__}:: starting...")
        self.action_matrix = {
            Economy.__name__: Economy(self.bot, self).start(),
            Researcher.__name__: Researcher(self.bot, self).start(),
            Attacker.__name__: Attacker(self.bot, self).start(),
            FleetManager.__name__: FleetManager(self.bot, self).start()
        }

        while not self.should_stop:
            logging.info(f"{self.__class__.__name__}:: Checking all planets...")

            for planet in self.bot.planets:
                logging.info(f"{self.__class__.__name__}:: Checking planet {planet.planet_id}...")

                # Todo implement random order

                planet_buildings = planet.get_planet_buildings()
                planet_defenses = planet.get_defense()

                time.sleep(self.SLEEPING_TIME_FACTOR * random.randint(1, 3))

            time.sleep(self.SLEEPING_TIME_FACTOR * random.randint(3, 10))
