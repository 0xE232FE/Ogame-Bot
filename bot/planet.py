import json
import re

from bs4 import BeautifulSoup

from lib.ogame import get_nbr, NOT_LOGGED


class Planet:
    def __init__(self, bot, planet_id):
        self.bot = bot
        self.planet_id = planet_id

    def fetch_resources(self, planet_id):
        url = self.bot.get_url('fetchResources', {'cp': planet_id})
        res = self.bot.session.get(url).content.decode('utf8')
        try:
            obj = json.loads(res)
        except ValueError:
            raise NOT_LOGGED
        return obj

    def get_resource_settings(self, planet_id):
        html = self.bot.session.get(self.bot.get_url('resourceSettings', {'cp': planet_id})).content
        if not self.bot.is_logged(html):
            raise NOT_LOGGED
        soup = BeautifulSoup(html, 'html.parser')
        options = soup.find_all('option', {'selected': True})
        res = {'metal_mine': options[0]['value'],
               'crystal_mine': options[1]['value'],
               'deuterium_synthesizer': options[2]['value'],
               'solar_plant': options[3]['value'],
               'fusion_reactor': options[4]['value'],
               'solar_satellite': options[5]['value']}
        return res

    def get_resources(self, planet_id):
        """Returns the planet resources stats."""
        resources = self.fetch_resources(planet_id)
        metal = resources['metal']['resources']['actual']
        crystal = resources['crystal']['resources']['actual']
        deuterium = resources['deuterium']['resources']['actual']
        energy = resources['energy']['resources']['actual']
        darkmatter = resources['darkmatter']['resources']['actual']
        result = {'metal': metal, 'crystal': crystal, 'deuterium': deuterium,
                  'energy': energy, 'darkmatter': darkmatter}
        return result

    def get_resources_buildings(self, planet_id):
        res = self.bot.session.get(self.bot.get_url('resources', {'cp': planet_id})).content
        if not self.bot.is_logged(res):
            raise NOT_LOGGED
        soup = BeautifulSoup(res, 'html.parser')
        res = {'metal_mine': get_nbr(soup, 'supply1'), 'crystal_mine': get_nbr(soup, 'supply2'),
               'deuterium_synthesizer': get_nbr(soup, 'supply3'), 'solar_plant': get_nbr(soup, 'supply4'),
               'fusion_reactor': get_nbr(soup, 'supply12'), 'solar_satellite': get_nbr(soup, 'supply212'),
               'metal_storage': get_nbr(soup, 'supply22'), 'crystal_storage': get_nbr(soup, 'supply23'),
               'deuterium_tank': get_nbr(soup, 'supply24')}
        return res

    def get_defense(self, planet_id):
        res = self.bot.session.get(self.bot.get_url('defense', {'cp': planet_id})).content
        if not self.bot.is_logged(res):
            raise NOT_LOGGED
        soup = BeautifulSoup(res, 'html.parser')
        res = {'rocket_launcher': get_nbr(soup, 'defense401'),
               'light_laser': get_nbr(soup, 'defense402'),
               'heavy_laser': get_nbr(soup, 'defense403'),
               'gauss_cannon': get_nbr(soup, 'defense404'),
               'ion_cannon': get_nbr(soup, 'defense405'),
               'plasma_turret': get_nbr(soup, 'defense406'),
               'small_shield_dome': get_nbr(soup, 'defense407'),
               'large_shield_dome': get_nbr(soup, 'defense408'),
               'anti_ballistic_missiles': get_nbr(soup, 'defense502'),
               'interplanetary_missiles': get_nbr(soup, 'defense503')}
        return res

    def get_ships(self, planet_id):
        res = self.bot.session.get(self.bot.get_url('shipyard', {'cp': planet_id})).content
        if not self.bot.is_logged(res):
            raise NOT_LOGGED
        soup = BeautifulSoup(res, 'html.parser')
        res = {'light_fighter': get_nbr(soup, 'military204'),
               'heavy_fighter': get_nbr(soup, 'military205'),
               'cruiser': get_nbr(soup, 'military206'),
               'battleship': get_nbr(soup, 'military207'),
               'battlecruiser': get_nbr(soup, 'military215'),
               'bomber': get_nbr(soup, 'military211'),
               'destroyer': get_nbr(soup, 'military213'),
               'deathstar': get_nbr(soup, 'military214'),
               'small_cargo': get_nbr(soup, 'civil202'),
               'large_cargo': get_nbr(soup, 'civil203'),
               'colony_ship': get_nbr(soup, 'civil208'),
               'recycler': get_nbr(soup, 'civil209'),
               'espionage_probe': get_nbr(soup, 'civil210'),
               'solar_satellite': get_nbr(soup, 'civil212')}
        return res

    def get_facilities(self, planet_id):
        res = self.bot.session.get(self.bot.get_url('station', {'cp': planet_id})).content
        if not self.bot.is_logged(res):
            raise NOT_LOGGED
        soup = BeautifulSoup(res, 'html.parser')
        res = {'robotics_factory': get_nbr(soup, 'station14'),
               'shipyard': get_nbr(soup, 'station21'),
               'research_lab': get_nbr(soup, 'station31'),
               'alliance_depot': get_nbr(soup, 'station34'),
               'missile_silo': get_nbr(soup, 'station44'),
               'nanite_factory': get_nbr(soup, 'station15'),
               'terraformer': get_nbr(soup, 'station33'),
               'space_dock': get_nbr(soup, 'station36')}
        return res

    def get_research(self):
        res = self.bot.session.get(self.bot.get_url('research')).content
        if not self.bot.is_logged(res):
            raise NOT_LOGGED
        soup = BeautifulSoup(res, 'html.parser')
        res = {'energy_technology': get_nbr(soup, 'research113'),
               'laser_technology': get_nbr(soup, 'research120'),
               'ion_technology': get_nbr(soup, 'research121'),
               'hyperspace_technology': get_nbr(soup, 'research114'),
               'plasma_technology': get_nbr(soup, 'research122'),
               'combustion_drive': get_nbr(soup, 'research115'),
               'impulse_drive': get_nbr(soup, 'research117'),
               'hyperspace_drive': get_nbr(soup, 'research118'),
               'espionage_technology': get_nbr(soup, 'research106'),
               'computer_technology': get_nbr(soup, 'research108'),
               'astrophysics': get_nbr(soup, 'research124'),
               'intergalactic_research_network': get_nbr(soup, 'research123'),
               'graviton_technology': get_nbr(soup, 'research199'),
               'weapons_technology': get_nbr(soup, 'research109'),
               'shielding_technology': get_nbr(soup, 'research110'),
               'armour_technology': get_nbr(soup, 'research111')}
        return res

    def constructions_being_built(self, planet_id):
        res = self.bot.session.get(self.bot.get_url('overview', {'cp': planet_id})).text
        if not self.bot.is_logged(res):
            raise NOT_LOGGED
        buildingCountdown = 0
        buildingID = 0
        researchCountdown = 0
        researchID = 0
        buildingCountdownMatch = re.search('getElementByIdWithCache\("Countdown"\),(\d+),', res)
        if buildingCountdownMatch:
            buildingCountdown = buildingCountdownMatch.group(1)
            buildingID = re.search('onclick="cancelProduction\((\d+),', res).group(1)
        researchCountdownMatch = re.search('getElementByIdWithCache\("researchCountdown"\),(\d+),', res)
        if researchCountdownMatch:
            researchCountdown = researchCountdownMatch.group(1)
            researchID = re.search('onclick="cancelResearch\((\d+),', res).group(1)
        return buildingID, buildingCountdown, researchID, researchCountdown
