import json
import re

from bs4 import BeautifulSoup

from lib.ogame import get_nbr, NOT_LOGGED
from lib.ogame.constants import Buildings, Ships, Resources


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
        res = {Buildings.MetalMine: options[0]['value'],
               Buildings.CrystalMine: options[1]['value'],
               Buildings.DeuteriumSynthesizer: options[2]['value'],
               Buildings.SolarPlant: options[3]['value'],
               Buildings.FusionReactor: options[4]['value'],
               Ships.SolarSatellite: options[5]['value']}
        return res

    def get_resources(self, planet_id):
        """Returns the planet resources stats."""
        resources = self.fetch_resources(planet_id)
        metal = resources['metal']['resources']['actual']
        crystal = resources['crystal']['resources']['actual']
        deuterium = resources['deuterium']['resources']['actual']
        energy = resources['energy']['resources']['actual']
        darkmatter = resources['darkmatter']['resources']['actual']
        return {Resources.Metal: metal,
                Resources.Crystal: crystal,
                Resources.Deuterium: deuterium,
                Resources.Energy: energy,
                Resources.DarkMatter: darkmatter}

    def get_resources_buildings(self, planet_id):
        res = self.bot.session.get(self.bot.get_url('resources', {'cp': planet_id})).content
        self.bot.is_logged(res)
        soup = BeautifulSoup(res, 'html.parser')
        res = {Buildings.MetalMine: get_nbr(soup, 'supply1'),
               Buildings.CrystalMine: get_nbr(soup, 'supply2'),
               Buildings.DeuteriumSynthesizer: get_nbr(soup, 'supply3'),
               Buildings.SolarPlant: get_nbr(soup, 'supply4'),
               Buildings.FusionReactor: get_nbr(soup, 'supply12'),
               Ships.SolarSatellite: get_nbr(soup, 'supply212'),
               Buildings.MetalStorage: get_nbr(soup, 'supply22'),
               Buildings.CrystalStorage: get_nbr(soup, 'supply23'),
               Buildings.DeuteriumTank: get_nbr(soup, 'supply24')}
        return res

    def get_defense(self, planet_id):
        res = self.bot.session.get(self.bot.get_url('defense', {'cp': planet_id})).content
        self.bot.is_logged(res)
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
        self.bot.is_logged(res)
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
        self.bot.is_logged(res)
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
        self.bot.is_logged(res)
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
        self.bot.is_logged(res)
        building_countdown = 0
        building_id = 0
        research_countdown = 0
        research_id = 0
        building_countdown_match = re.search('getElementByIdWithCache\("Countdown"\),(\d+),', res)
        if building_countdown_match:
            building_countdown = building_countdown_match.group(1)
            building_id = re.search('onclick="cancelProduction\((\d+),', res).group(1)
        research_countdown_match = re.search('getElementByIdWithCache\("research_countdown"\),(\d+),', res)
        if research_countdown_match:
            research_countdown = research_countdown_match.group(1)
            research_id = re.search('onclick="cancelResearch\((\d+),', res).group(1)
        return building_id, building_countdown, research_id, research_countdown
