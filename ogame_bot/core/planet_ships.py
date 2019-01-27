from bs4 import BeautifulSoup

from ogame_bot import get_bot, retry_if_logged_out
from ogame_bot.lib.ogame import get_nbr
from ogame_bot.lib.ogame.constants import Ships


class PlanetShips:
    def __init__(self, planet):
        self.bot = get_bot()
        self.planet = planet

    @retry_if_logged_out
    def get_ships(self):
        res = self.bot.wrapper.session.get(self.bot.get_url('shipyard', {'cp': self.planet.planet_id})).content
        self.bot.is_logged(res)
        soup = BeautifulSoup(res, 'html.parser')
        return {Ships.LightFighter: get_nbr(soup, 'military204'),
                Ships.HeavyFighter: get_nbr(soup, 'military205'),
                Ships.Cruiser: get_nbr(soup, 'military206'),
                Ships.Battleship: get_nbr(soup, 'military207'),
                Ships.Battlecruiser: get_nbr(soup, 'military215'),
                Ships.Bomber: get_nbr(soup, 'military211'),
                Ships.Destroyer: get_nbr(soup, 'military213'),
                Ships.Deathstar: get_nbr(soup, 'military214'),
                Ships.SmallCargo: get_nbr(soup, 'civil202'),
                Ships.LargeCargo: get_nbr(soup, 'civil203'),
                Ships.ColonyShip: get_nbr(soup, 'civil208'),
                Ships.Recycler: get_nbr(soup, 'civil209'),
                Ships.EspionageProbe: get_nbr(soup, 'civil210'),
                Ships.SolarSatellite: get_nbr(soup, 'civil212')}

    def get_military_ships(self, without_cargo=True, ships=None):
        if not ships:
            ships = self.get_ships()
        ships.pop(Ships.ColonyShip)
        ships.pop(Ships.SolarSatellite)
        ships.pop(Ships.EspionageProbe)
        ships.pop(Ships.Recycler)
        if without_cargo:
            ships.pop(Ships.SmallCargo)
            ships.pop(Ships.LargeCargo)
        return ships

    def get_civilian_ships(self, with_probe=False, ships=None):
        if not ships:
            ships = self.get_ships()

        civilian_ships = {
            Ships.ColonyShip: ships[Ships.ColonyShip],
            Ships.Recycler: ships[Ships.Recycler],
            Ships.SmallCargo: ships[Ships.SmallCargo],
            Ships.LargeCargo: ships[Ships.LargeCargo]
        }

        if with_probe:
            civilian_ships[Ships.EspionageProbe] = ships[Ships.EspionageProbe]

        return civilian_ships

    @staticmethod
    def has_ships(ships):
        return any(ships.values())
