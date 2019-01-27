import logging
import random
import time

from ogame_bot.fleet import Fleet
from ogame_bot.galaxy import Galaxy
from ogame_bot.modes.mode import Mode
from ogame_bot.ogame.constants import Speed, Resources, Missions, Coords, TargetTypes
from ogame_bot.util import convert_constant_name


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

                ships = planet.planet_ships.get_military_ships(without_cargo=False)

                # if some ships can be send
                if planet.planet_ships.has_ships(ships):
                    prepared_ships = {
                        convert_constant_name(ship.name): ships[ship]
                        for ship in ships
                    }
                    planet_info = self.bot.galaxy.get_planet_infos(planet.planet_id)['coordinate']
                    logging.info(f"{self.__class__.__name__}:: Try sending {prepared_ships} from {planet_info}")
                    result = self.bot.fleet.send_fleet(planet.planet_id,
                                                       prepared_ships,
                                                       Speed.HUNDRED_PERCENT,
                                                       {
                                                           Coords.Galaxy.value: planet_info[Coords.Galaxy.value],
                                                           Coords.System.value: planet_info[Coords.System.value],
                                                           Coords.Position.value: 16,
                                                           Coords.Type.value: TargetTypes.Planet
                                                       },
                                                       Missions.Expedition,
                                                       {
                                                           Resources.Metal.value: 0,
                                                           Resources.Crystal.value: 0,
                                                           Resources.Deuterium.value: 0
                                                       })
                    if result is not None:
                        logging.info(f"{self.__class__.__name__}:: Sent to {planet_info[Coords.Galaxy.value]}:{planet_info[Coords.System.value]}:16")

            time.sleep(self.SLEEPING_TIME_FACTOR * random.randint(1, 10))
