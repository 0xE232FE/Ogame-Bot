import logging
import random
import time

from ogame_bot.fleet import Fleet
from ogame_bot.galaxy import Galaxy
from ogame_bot.modes.mode import Mode
from ogame_bot.ogame.constants import Speed, Resources, Missions, Coords, TargetTypes
from ogame_bot.util import convert_constant_name


class BalancedMode(Mode):
    SLEEPING_TIME_FACTOR = 60

    def __init__(self, bot, session):
        super().__init__(bot, session)

    def run(self):
        logging.info(f"{self.__class__.__name__}:: starting...")
        while not self.should_stop:
            logging.info(f"{self.__class__.__name__}:: Checking all planets...")

            for planet in self.bot.planets:
                logging.info(f"{self.__class__.__name__}:: Checking planet {planet.planet_id}...")

                # Todo implement random order
                ships = planet.planet_ships.get_ships()
                military_ships = planet.planet_ships.get_military_ships(without_cargo=False, ships=ships)
                civilian_ships = planet.planet_ships.get_civilian_ships(with_probe=True, ships=ships)
                planet_buildings = planet.get_planet_buildings()
                planet_defenses = planet.get_defense()

                # choose a random action
                # Todo improve random factor with priority
                action = random.randint(1, 4)
                if action == 1:
                    action_re

                time.sleep(self.SLEEPING_TIME_FACTOR * random.randint(1, 3))

            time.sleep(self.SLEEPING_TIME_FACTOR * random.randint(3, 10))

    def action_build_army(self):
        pass

    def action_research(self):
        pass

    def action_economy(self):
        pass

    def action_attack(self):
        pass
