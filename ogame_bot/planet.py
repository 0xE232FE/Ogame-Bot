import json
import logging
import re

from bs4 import BeautifulSoup

from ogame_bot import get_bot, retry_if_logged_out
from ogame_bot.builder import Builder
from ogame_bot.ogame import get_nbr
from ogame_bot.ogame.constants import Buildings, Ships, Resources, Defenses, Facilities, Research
from ogame_bot.planet_ships import PlanetShips


class Planet:
    def __init__(self, planet_id):
        self.bot = get_bot()
        self.planet_id = planet_id
        self.builder = Builder(self)
        self.planet_ships = PlanetShips(self)

    @retry_if_logged_out
    def fetch_resources(self):
        url = self.bot.get_url('fetchResources', {'cp': self.planet_id})
        res = self.bot.wrapper.session.get(url).content.decode('utf8')
        self.bot.is_logged()
        try:
            return json.loads(res)
        except ValueError:
            logging.warning(f"{self.__class__.__name__}:: Disconnected...")
            return {}

    @retry_if_logged_out
    def get_resource_settings(self):
        html = self.bot.wrapper.session.get(self.bot.get_url('resourceSettings', {'cp': self.planet_id})).content
        self.bot.is_logged(html)
        soup = BeautifulSoup(html, 'html.parser')
        options = soup.find_all('option', {'selected': True})
        res = {Buildings.MetalMine: options[0]['value'],
               Buildings.CrystalMine: options[1]['value'],
               Buildings.DeuteriumSynthesizer: options[2]['value'],
               Buildings.SolarPlant: options[3]['value'],
               Buildings.FusionReactor: options[4]['value'],
               Ships.SolarSatellite: options[5]['value']}
        return res

    @retry_if_logged_out
    def get_resources(self):
        """Returns the planet resources stats."""
        resources = self.fetch_resources()
        self.bot.is_logged()
        return {Resources.Metal: resources['metal']['resources']['actual'],
                Resources.Crystal: resources['crystal']['resources']['actual'],
                Resources.Deuterium: resources['deuterium']['resources']['actual'],
                Resources.Energy: resources['energy']['resources']['actual'],
                Resources.DarkMatter: resources['darkmatter']['resources']['actual']}

    @retry_if_logged_out
    def get_resources_buildings(self):
        res = self.bot.wrapper.session.get(self.bot.get_url('resources', {'cp': self.planet_id})).content
        self.bot.is_logged(res)
        soup = BeautifulSoup(res, 'html.parser')
        return {Buildings.MetalMine: get_nbr(soup, 'supply1'),
                Buildings.CrystalMine: get_nbr(soup, 'supply2'),
                Buildings.DeuteriumSynthesizer: get_nbr(soup, 'supply3'),
                Buildings.SolarPlant: get_nbr(soup, 'supply4'),
                Buildings.FusionReactor: get_nbr(soup, 'supply12'),
                Ships.SolarSatellite: get_nbr(soup, 'supply212'),
                Buildings.MetalStorage: get_nbr(soup, 'supply22'),
                Buildings.CrystalStorage: get_nbr(soup, 'supply23'),
                Buildings.DeuteriumTank: get_nbr(soup, 'supply24')}

    @retry_if_logged_out
    def get_defense(self):
        res = self.bot.wrapper.session.get(self.bot.get_url('defense', {'cp': self.planet_id})).content
        self.bot.is_logged(res)
        soup = BeautifulSoup(res, 'html.parser')
        return {Defenses.RocketLauncher: get_nbr(soup, 'defense401'),
                Defenses.LightLaser: get_nbr(soup, 'defense402'),
                Defenses.HeavyLaser: get_nbr(soup, 'defense403'),
                Defenses.GaussCannon: get_nbr(soup, 'defense404'),
                Defenses.IonCannon: get_nbr(soup, 'defense405'),
                Defenses.PlasmaTurret: get_nbr(soup, 'defense406'),
                Defenses.SmallShieldDome: get_nbr(soup, 'defense407'),
                Defenses.LargeShieldDome: get_nbr(soup, 'defense408'),
                Defenses.AntiBallisticMissiles: get_nbr(soup, 'defense502'),
                Defenses.InterplanetaryMissiles: get_nbr(soup, 'defense503')}

    @retry_if_logged_out
    def get_facilities(self):
        res = self.bot.wrapper.session.get(self.bot.get_url('station', {'cp': self.planet_id})).content
        self.bot.is_logged(res)
        soup = BeautifulSoup(res, 'html.parser')
        return {Facilities.RoboticsFactory: get_nbr(soup, 'station14'),
                Facilities.Shipyard: get_nbr(soup, 'station21'),
                Facilities.ResearchLab: get_nbr(soup, 'station31'),
                Facilities.AllianceDepot: get_nbr(soup, 'station34'),
                Facilities.MissileSilo: get_nbr(soup, 'station44'),
                Facilities.NaniteFactory: get_nbr(soup, 'station15'),
                Facilities.Terraformer: get_nbr(soup, 'station33'),
                Facilities.SpaceDock: get_nbr(soup, 'station36')}

    @retry_if_logged_out
    def get_research(self):
        res = self.bot.wrapper.session.get(self.bot.get_url('research')).content
        self.bot.is_logged(res)
        soup = BeautifulSoup(res, 'html.parser')
        return {Research.EnergyTechnology: get_nbr(soup, 'research113'),
                Research.LaserTechnology: get_nbr(soup, 'research120'),
                Research.IonTechnology: get_nbr(soup, 'research121'),
                Research.HyperspaceTechnology: get_nbr(soup, 'research114'),
                Research.PlasmaTechnology: get_nbr(soup, 'research122'),
                Research.CombustionDrive: get_nbr(soup, 'research115'),
                Research.ImpulseDrive: get_nbr(soup, 'research117'),
                Research.HyperspaceDrive: get_nbr(soup, 'research118'),
                Research.EspionageTechnology: get_nbr(soup, 'research106'),
                Research.ComputerTechnology: get_nbr(soup, 'research108'),
                Research.Astrophysics: get_nbr(soup, 'research124'),
                Research.IntergalacticResearchNetwork: get_nbr(soup, 'research123'),
                Research.GravitonTechnology: get_nbr(soup, 'research199'),
                Research.WeaponsTechnology: get_nbr(soup, 'research109'),
                Research.ShieldingTechnology: get_nbr(soup, 'research110'),
                Research.ArmourTechnology: get_nbr(soup, 'research111')}

    def get_planet_buildings(self):
        return {
            **self.get_resources_buildings(),
            **self.get_facilities(),
            **self.get_research()
        }

    def get_planet_ships_and_defenses(self):
        return {
            **self.planet_ships.get_ships(),
            **self.get_defense()
        }

    @retry_if_logged_out
    def constructions_being_built(self):
        res = self.bot.wrapper.session.get(self.bot.get_url('overview', {'cp': self.planet_id})).text
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
