import logging
import random
import time

from ogame_bot.lib.ogame.constants import Buildings, Facilities, Research

from ogame_bot.modes.mode import Mode


class StarterBuilderMode(Mode):
    SLEEPING_TIME_FACTOR = 60 / 10  # normal value = 60 --> minutes

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
                                 Buildings.SolarPlant, Facilities.ResearchLab, Facilities.Shipyard,
                                 Research.EnergyTechnology, Research.CombustionDrive, Research.LaserTechnology,
                                 Research.ComputerTechnology, Research.EspionageTechnology]

                planet_buildings = planet.get_planet_buildings()

                for _ in range(1, random.randint(2, 20)):
                    building = random.choice(dict_to_build)
                    if (planet.builder.can_build(building,
                                                 planet_buildings=planet_buildings,
                                                 build_if_can=True)):
                        logging.info(f"{self.__class__.__name__}:: Start building {building}...")
                    time.sleep(random.randint(2, 60))

            time.sleep(self.SLEEPING_TIME_FACTOR * random.randint(2, 30))
