import math

from bs4 import BeautifulSoup

from lib.ogame import BAD_RESEARCH_ID, constants, BAD_DEFENSE_ID, BAD_SHIP_ID, BAD_BUILDING_ID, Calculate
from lib.ogame.constants import Resources


class Builder:
    def __init__(self, bot, planet):
        self.bot = bot
        self.planet = planet

    def build_defense(self, defense_id, nbr):
        """Build a defense unit."""
        if defense_id not in constants.Defense:
            raise BAD_DEFENSE_ID

        url = self.bot.get_url('defense', {'cp': self.planet.planet_id})

        res = self.bot.session.get(url).content
        self.bot.is_logged(res)
        soup = BeautifulSoup(res, 'html.parser')
        form = soup.find('form')
        token = form.find('input', {'name': 'token'}).get('value')

        payload = {'menge': nbr,
                   'modus': 1,
                   'token': token,
                   'type': defense_id}
        self.bot.session.post(url, data=payload)

    def build_ships(self, ship_id, nbr):
        """Build a ship unit."""
        if ship_id not in constants.Ships:
            raise BAD_SHIP_ID

        url = self.bot.get_url('shipyard', {'cp': self.planet.planet_id})

        res = self.bot.session.get(url).content
        self.bot.is_logged(res)
        soup = BeautifulSoup(res, 'html.parser')
        form = soup.find('form')
        token = form.find('input', {'name': 'token'}).get('value')

        payload = {'menge': nbr,
                   'modus': 1,
                   'token': token,
                   'type': ship_id}
        self.bot.session.post(url, data=payload)

    def build_building(self, building_id, cancel=False):
        """Build a building."""
        if building_id not in constants.Buildings and building_id not in constants.Facilities:
            raise BAD_BUILDING_ID

        url = self.bot.get_url('resources', {'cp': self.planet.planet_id})

        res = self.bot.session.get(url).content
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
        self.bot.session.post(url, data=payload)
        # return True

    def building_cost(self, building, lvl):
        """ Building cost lvl + 1 """
        return {
            Resources.Metal: int(math.floor(Calculate[building]['cost'][Resources.Metal][0] *
                                            Calculate[building]['cost'][Resources.Metal][1] ** (lvl - 1))),
            Resources.Crystal: int(math.floor(Calculate[building]['cost'][Resources.Crystal][0] *
                                              Calculate[building]['cost'][Resources.Crystal][1] ** (lvl - 1))),
            Resources.Deuterium: int(math.floor(Calculate[building]['cost'][Resources.Deuterium][0] *
                                                Calculate[building]['cost'][Resources.Deuterium][1] ** (lvl - 1)))
        }

    def can_build(self, building, lvl, build_if_can=True) -> bool:
        build_requirements = self.building_cost(building, lvl)
        planet_resources = self.planet.get_resources()
        if planet_resources[Resources.Metal] >= build_requirements[Resources.Metal] and \
                planet_resources[Resources.Metal] >= build_requirements[Resources.Metal] and \
                planet_resources[Resources.Metal] >= build_requirements[Resources.Metal]:
            if build_if_can:
                self._build(building)
            return True
        return False

    def build_technology(self, technology_id, cancel=False):
        if technology_id not in constants.Research:
            raise BAD_RESEARCH_ID

        url = self.bot.get_url('research', {'cp': self.planet.planet_id})
        modus = 2 if cancel else 1
        payload = {'modus': modus,
                   'type': technology_id}
        res = self.bot.session.post(url, data=payload).content
        self.bot.is_logged(res)

    def _build(self, object_id, nbr=None, cancel=False):
        if object_id in constants.Buildings or object_id in constants.Facilities:
            self.build_building(object_id, cancel=cancel)
        elif object_id in constants.Research:
            self.build_technology(object_id, cancel=cancel)
        elif object_id in constants.Ships:
            self.build_ships(object_id, nbr)
        elif object_id in constants.Defense:
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
