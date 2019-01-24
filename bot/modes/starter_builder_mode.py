import logging
import random
import time

from lib.ogame.constants import Buildings, Facilities, Research

from bot.modes.mode import Mode


class StarterBuilderMode(Mode):
    SLEEPING_TIME_FACTOR = 1

    def __init__(self, bot, session):
        super().__init__(bot, session)

    def run(self):
        logging.info(f"{self.__class__.__name__}:: starting...")
        while not self.should_stop:
            logging.info(f"{self.__class__.__name__}:: Checking all planets...")

            for planet in self.bot.planets:
                logging.info(f"{self.__class__.__name__}:: Checking planet {planet.planet_id}...")

                dict_to_build = [Buildings.MetalStorage, Buildings.MetalMine, Buildings.CrystalStorage,
                                 Buildings.CrystalMine, Buildings.DeuteriumTank, Buildings.DeuteriumSynthesizer,
                                 Buildings.SolarPlant, Facilities.ResearchLab, Facilities.Shipyard]

                planet_buildings_level = {**planet.get_resources_buildings(), **planet.get_facilities()}

                for _ in range(1, random.randint(2, 20)):
                    building = random.choice(dict_to_build)
                    if (planet.builder.can_build(building,
                                                 lvl=planet_buildings_level[building] + 1,
                                                 planet_resources=None,
                                                 build_if_can=True)):
                        logging.info(f"{self.__class__.__name__}:: Start building {building}...")
                    time.sleep(random.randint(10, 30))

            time.sleep(self.SLEEPING_TIME_FACTOR * random.randint(2, 25))
