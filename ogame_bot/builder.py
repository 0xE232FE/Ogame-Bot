import math

from bs4 import BeautifulSoup

from ogame_bot import get_bot, retry_if_logged_out
from lib.ogame import BAD_RESEARCH_ID, constants, BAD_DEFENSE_ID, BAD_SHIP_ID, BAD_BUILDING_ID
from lib.ogame.constants import Resources, Prices, Ships, Defenses


class Builder:
    def __init__(self, planet):
        self.bot = get_bot()
        self.planet = planet

    @retry_if_logged_out
    def build_defense(self, defense_id, nbr):
        """Build a defense unit."""
        if defense_id not in constants.Defenses:
            raise BAD_DEFENSE_ID
        else:
            defense_id = defense_id.value

        url = self.bot.get_url('defense', {'cp': self.planet.planet_id})

        res = self.bot.wrapper.session.get(url).content
        self.bot.is_logged(res)
        soup = BeautifulSoup(res, 'html.parser')
        form = soup.find('form')
        token = form.find('input', {'name': 'token'}).get('value')

        payload = {'menge': nbr,
                   'modus': 1,
                   'token': token,
                   'type': defense_id}
        self.bot.wrapper.session.post(url, data=payload)

    @retry_if_logged_out
    def build_ships(self, ship_id, nbr):
        """Build a ship unit."""
        if ship_id not in constants.Ships:
            raise BAD_SHIP_ID
        else:
            ship_id = ship_id.value

        url = self.bot.get_url('shipyard', {'cp': self.planet.planet_id})

        res = self.bot.wrapper.session.get(url).content
        self.bot.is_logged(res)
        soup = BeautifulSoup(res, 'html.parser')
        form = soup.find('form')
        token = form.find('input', {'name': 'token'}).get('value')

        payload = {'menge': nbr,
                   'modus': 1,
                   'token': token,
                   'type': ship_id}
        self.bot.wrapper.session.post(url, data=payload)

    @retry_if_logged_out
    def build_building(self, building_id, cancel=False):
        """Build a building."""
        if building_id not in constants.Buildings and building_id not in constants.Facilities:
            raise BAD_BUILDING_ID
        else:
            building_id = building_id.value

        url = self.bot.get_url('resources', {'cp': self.planet.planet_id})

        res = self.bot.wrapper.session.get(url).content
        self.bot.is_logged(res)
        soup = BeautifulSoup(res, 'html.parser')
        # is_idle = bool(soup.find('td', {'class': 'idle'}))
        # if not is_idle:
        #     return False
        form = soup.find('form')
        token = form.find('input', {'name': 'token'}).get('value')
        modus = 2 if cancel else 1
        payload = {'modus': modus,
                   'token': token,
                   'type': building_id}
        self.bot.wrapper.session.post(url, data=payload)
        # return True

    @retry_if_logged_out
    def build_technology(self, technology_id, cancel=False):
        if technology_id not in constants.Research:
            raise BAD_RESEARCH_ID
        else:
            technology_id = technology_id.value

        url = self.bot.get_url('research', {'cp': self.planet.planet_id})
        modus = 2 if cancel else 1
        payload = {'modus': modus,
                   'type': technology_id}
        res = self.bot.wrapper.session.post(url, data=payload).content
        self.bot.is_logged(res)

    def construction_time(self):
        pass  # TODO https://ogame.fandom.com/wiki/Buildings

    @staticmethod
    def building_cost(building, lvl):
        """ Building cost lvl + 1 """
        return {
            Resources.Metal: int(math.floor(Prices[building]['cost'][Resources.Metal][0] *
                                            Prices[building]['cost'][Resources.Metal][1] ** (lvl - 1))),
            Resources.Crystal: int(math.floor(Prices[building]['cost'][Resources.Crystal][0] *
                                              Prices[building]['cost'][Resources.Crystal][1] ** (lvl - 1))),
            Resources.Deuterium: int(math.floor(Prices[building]['cost'][Resources.Deuterium][0] *
                                                Prices[building]['cost'][Resources.Deuterium][1] ** (lvl - 1)))
        }

    @staticmethod
    def building_prerequisites(building, planet_buildings):
        if 'prerequisites' in Prices[building]:
            status = True
            for prerequisite in Prices[building]['prerequisites']:
                if prerequisite['building'] not in planet_buildings or \
                        planet_buildings[building] < prerequisite['level']:
                    status = False
            return status
        else:
            return True

    def can_build(self, building, nbr=1, planet_resources=None, planet_buildings=None, build_if_can=True) -> bool:
        lvl = 0

        if not planet_buildings:
            planet_buildings = self.planet.get_planet_buildings()

        if building not in Ships and building not in Defenses:
            try:
                lvl = planet_buildings[building] + 1
            except KeyError:
                lvl = 1

        build_requirements = self.building_cost(building, lvl)

        if not planet_resources:
            planet_resources = self.planet.get_resources()

        if planet_resources[Resources.Metal] >= build_requirements[Resources.Metal] and \
                planet_resources[Resources.Metal] >= build_requirements[Resources.Metal] and \
                planet_resources[Resources.Metal] >= build_requirements[Resources.Metal] and \
                self.building_prerequisites(building, planet_buildings):
            if build_if_can:
                if building in Ships or building in Defenses:
                    self._build(building, nbr=nbr)
                else:
                    self._build(building)
            return True
        return False

    def _build(self, object_id, nbr=None, cancel=False):
        if object_id in constants.Buildings or object_id in constants.Facilities:
            self.build_building(object_id, cancel=cancel)
        elif object_id in constants.Research:
            self.build_technology(object_id, cancel=cancel)
        elif object_id in constants.Ships:
            self.build_ships(object_id, nbr)
        elif object_id in constants.Defenses:
            self.build_defense(object_id, nbr)

    def build(self, arg, cancel=False):
        if isinstance(arg, list):
            for element in arg:
                self.build(element, cancel=cancel)
        elif isinstance(arg, tuple):
            elem_id, nbr = arg
            self._build(elem_id, nbr, cancel=cancel)
        else:
            elem_id = arg
            self._build(elem_id, cancel=cancel)
