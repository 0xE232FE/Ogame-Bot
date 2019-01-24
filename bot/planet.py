import json
import re

from bs4 import BeautifulSoup

from bot.builder import Builder
from lib.ogame import get_nbr, NOT_LOGGED
from lib.ogame.constants import Buildings, Ships, Resources, Defenses, Facilities, Research


class Planet:
    def __init__(self, bot, planet_id):
        self.bot = bot
        self.planet_id = planet_id
        self.builder = Builder(self.bot, self)

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
        return {Resources.Metal: resources['metal']['resources']['actual'],
                Resources.Crystal: resources['crystal']['resources']['actual'],
                Resources.Deuterium: resources['deuterium']['resources']['actual'],
                Resources.Energy: resources['energy']['resources']['actual'],
                Resources.DarkMatter: resources['darkmatter']['resources']['actual']}

    def get_resources_buildings(self, planet_id):
        res = self.bot.session.get(self.bot.get_url('resources', {'cp': planet_id})).content
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

    def get_defense(self, planet_id):
        res = self.bot.session.get(self.bot.get_url('defense', {'cp': planet_id})).content
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

    def get_ships(self, planet_id):
        res = self.bot.session.get(self.bot.get_url('shipyard', {'cp': planet_id})).content
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

    def get_facilities(self, planet_id):
        res = self.bot.session.get(self.bot.get_url('station', {'cp': planet_id})).content
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

    def get_research(self):
        res = self.bot.session.get(self.bot.get_url('research')).content
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
