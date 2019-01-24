import math

from bs4 import BeautifulSoup

from lib.ogame import BAD_RESEARCH_ID, constants, BAD_DEFENSE_ID, BAD_SHIP_ID, BAD_BUILDING_ID, Calculate


class Builder:
    def __init__(self, bot, planet):
        self.bot = bot
        self.planet = planet

    def build_defense(self, planet_id, defense_id, nbr):
        """Build a defense unit."""
        if defense_id not in constants.Defense:
            raise BAD_DEFENSE_ID

        url = self.bot.get_url('defense', {'cp': planet_id})

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

    def build_ships(self, planet_id, ship_id, nbr):
        """Build a ship unit."""
        if ship_id not in constants.Ships:
            raise BAD_SHIP_ID

        url = self.bot.get_url('shipyard', {'cp': planet_id})

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

    def build_building(self, planet_id, building_id, cancel=False):
        """Build a building."""
        if building_id not in constants.Buildings and building_id not in constants.Facilities:
            raise BAD_BUILDING_ID

        url = self.bot.get_url('resources', {'cp': planet_id})

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

    def building_cost(self, category, building, lvl):
        """ Building cost lvl + 1 """
        cost = {'Metal': int(math.floor(Calculate[category][building]['cost']['Metal'][0] *
                                        Calculate[category][building]['cost']['Metal'][1] ** (lvl - 1))),
                'Crystal': int(math.floor(Calculate[category][building]['cost']['Crystal'][0] *
                                          Calculate[category][building]['cost']['Crystal'][1] ** (lvl - 1))),
                'Deuterium': int(math.floor(Calculate[category][building]['cost']['Deuterium'][0] *
                                            Calculate[category][building]['cost']['Deuterium'][1] ** (lvl - 1)))
                }
        return cost

    def can_build(self):
        pass # TODO

    def build_technology(self, planet_id, technology_id, cancel=False):
        if technology_id not in constants.Research:
            raise BAD_RESEARCH_ID

        url = self.bot.get_url('research', {'cp': planet_id})
        modus = 2 if cancel else 1
        payload = {'modus': modus,
                   'type': technology_id}
        res = self.bot.session.post(url, data=payload).content
        self.bot.is_logged(res)

    def _build(self, planet_id, object_id, nbr=None, cancel=False):
        if object_id in constants.Buildings or object_id in constants.Facilities:
            self.build_building(planet_id, object_id, cancel=cancel)
        elif object_id in constants.Research:
            self.build_technology(planet_id, object_id, cancel=cancel)
        elif object_id in constants.Ships:
            self.build_ships(planet_id, object_id, nbr)
        elif object_id in constants.Defense:
            self.build_defense(planet_id, object_id, nbr)

    def build(self, planet_id, arg, cancel=False):
        if isinstance(arg, list):
            for element in arg:
                self.build(planet_id, element, cancel=cancel)
        elif isinstance(arg, tuple):
            elem_id, nbr = arg
            self._build(planet_id, elem_id, nbr, cancel=cancel)
        else:
            elem_id = arg
            self._build(planet_id, elem_id, cancel=cancel)
