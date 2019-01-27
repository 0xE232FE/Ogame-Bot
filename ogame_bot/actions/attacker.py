import logging

from ogame_bot.actions.action import Action
from ogame_bot.ogame.constants import Coords, TargetTypes, Missions, Resources, Speed
from ogame_bot.util import convert_constant_name


class Attacker(Action):
    def __init__(self, bot, mode):
        super().__init__(bot, mode)

    def perform_action(self, planet):
        ships = planet.planet_ships.get_ships()
        military_ships = planet.planet_ships.get_military_ships(without_cargo=False, ships=ships)
        civilian_ships = planet.planet_ships.get_civilian_ships(with_probe=True, ships=ships)

        self.create_expedition(planet, military_ships)

    def create_expedition(self, planet, military_ships):
        # if some ships can be send
        if planet.planet_ships.has_ships(military_ships):
            prepared_ships = {
                convert_constant_name(ship.name): military_ships[ship]
                for ship in military_ships
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
