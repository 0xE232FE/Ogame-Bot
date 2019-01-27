import logging
import random
import re

from bs4 import BeautifulSoup

from old_python.ogame_bot import get_bot, retry_if_logged_out
from old_python.ogame_bot.lib.ogame import parse_int
from old_python.ogame_bot.lib.ogame import Me


class User:
    def __init__(self):
        self.bot = get_bot()

    @retry_if_logged_out
    def get_user_infos(self, html=None):
        if not html:
            html = self.bot.wrapper.session.get(self.bot.get_url('overview')).content
        self.bot.is_logged(html)
        soup = BeautifulSoup(re.search(r'textContent\[7\]="([^"]+)"', html).group(1), 'html.parser')
        infos = re.search(r'([\d\\.]+) \(Place ([\d\.]+) of ([\d\.]+)\)', soup.text)
        return {
            Me.id: int(re.search(r'playerId="(\w+)"', html).group(1)),
            Me.Name: re.search(r'playerName="([^"]+)"', html).group(1),
            Me.HonourPoints: parse_int(re.search(r'textContent\[9\]="([^"]+)"', html).group(1)),
            Me.PlanetsId: self.get_planet_ids(html),
            Me.Points: parse_int(infos.group(1)),
            Me.Rank: parse_int(infos.group(2)),
            Me.Total: parse_int(infos.group(3))
        }

    @retry_if_logged_out
    def get_planet_ids(self, res=None):
        """Get the ids of your planets."""
        if not res:
            res = self.bot.wrapper.session.get(self.bot.get_url('overview')).content
        self.bot.is_logged(res)
        soup = BeautifulSoup(res, 'html.parser')
        planets = soup.findAll('div', {'class': 'smallplanet'})
        return [planet['id'].replace('planet-', '') for planet in planets]

    @retry_if_logged_out
    def get_moon_ids(self, res=None):
        """Get the ids of your moons."""
        if not res:
            res = self.bot.wrapper.session.get(self.bot.get_url('overview')).content
        self.bot.is_logged(res)
        soup = BeautifulSoup(res, 'html.parser')
        moons = soup.findAll('a', {'class': 'moonlink'})
        return [moon['href'].split('&cp=')[1] for moon in moons]

    @retry_if_logged_out
    def get_planet_by_name(self, planet_name, res=None):
        """Returns the first planet id with the specified name."""
        if not res:
            res = self.bot.wrapper.session.get(self.bot.get_url('overview')).content
        self.bot.is_logged(res)
        soup = BeautifulSoup(res, 'html.parser')
        planets = soup.findAll('div', {'class': 'smallplanet'})
        for planet in planets:
            title = planet.find('a', {'class': 'planetlink'}).get('title')
            name = re.search(r'<b>(.+) \[(\d+):(\d+):(\d+)\]</b>', title).groups()[0]
            if name == planet_name:
                planet_id = planet['id'].replace('planet-', '')
                return planet_id
        return None

    def get_random_player_planet(self):
        return self.bot.planets[random.randint(0, len(self.bot.planets) - 1)]

    def is_under_attack(self, json_obj=None):
        if not json_obj:
            json_obj = self.bot.fetch_eventbox()
        return not json_obj.get('hostile', 0) == 0

    def get_attacks(self):
        headers = {'X-Requested-With': 'XMLHttpRequest'}
        res = self.bot.wrapper.session.get(self.bot.get_url('eventList'), params={'ajax': 1},
                                           headers=headers).content
        soup = BeautifulSoup(res, 'html.parser')
        if soup.find('head'):
            logging.warning(f"{self.__class__.__name__}:: Disconnected...")
        events = soup.findAll('tr', {'class': 'eventFleet'})
        events = filter(lambda x: 'partnerInfo' not in x.get('class', []), events)
        events += soup.findAll('tr', {'class': 'allianceAttack'})
        attacks = []
        for event in events:
            mission_type = int(event['data-mission-type'])
            if mission_type not in [1, 2]:
                continue

            attack = {}
            attack.update({'mission_type': mission_type})
            if mission_type == 1:
                coords_origin = event.find('td', {'class': 'coordsOrigin'}) \
                    .text.strip()
                coords = re.search(r'\[(\d+):(\d+):(\d+)\]', coords_origin)
                galaxy, system, position = coords.groups()
                attack.update({'origin': (int(galaxy), int(system), int(position))})
            else:
                attack.update({'origin': None})

            dest_coords = event.find('td', {'class': 'destCoords'}).text.strip()
            coords = re.search(r'\[(\d+):(\d+):(\d+)\]', dest_coords)
            galaxy, system, position = coords.groups()
            attack.update({'destination': (int(galaxy), int(system), int(position))})

            arrival_time = event.find('td', {'class': 'arrivalTime'}).text.strip()
            coords = re.search(r'(\d+):(\d+):(\d+)', arrival_time)
            hour, minute, second = coords.groups()
            hour = int(hour)
            minute = int(minute)
            second = int(second)
            arrival_time = self.get_datetime_from_time(hour, minute, second)
            attack.update({'arrival_time': arrival_time})

            if mission_type == 1:
                attacker_id = event.find('a', {'class': 'sendMail'})['data-playerid']
                attack.update({'attacker_id': int(attacker_id)})
            else:
                attack.update({'attacker_id': None})

            attacks.append(attack)
        return attacks
