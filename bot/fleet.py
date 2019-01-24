import re

from bs4 import BeautifulSoup

from lib.ogame import parse_int, NOT_LOGGED, constants, get_code


class Fleet:
    def __init__(self):
        pass

    def send_fleet(self, planet_id, ships, speed, where, mission, resources):
        def get_hidden_fields(html):
            soup = BeautifulSoup(html, 'html.parser')
            inputs = soup.findAll('input', {'type': 'hidden'})
            fields = {}
            for input_element in inputs:
                name = input_element.get('name')
                value = input_element.get('value')
                fields[name] = value
            return fields

        url = self.get_url('fleet1', {'cp': planet_id})

        res = self.session.get(url).content
        if not self.is_logged(res):
            raise NOT_LOGGED
        payload = {}
        payload.update(get_hidden_fields(res))
        for name, value in ships:
            payload['am{}'.format(name)] = value
        res = self.session.post(self.get_url('fleet2'), data=payload).content

        payload = {}
        payload.update(get_hidden_fields(res))
        payload.update({'speed': speed,
                        'galaxy': where.get('galaxy'),
                        'system': where.get('system'),
                        'position': where.get('position'),
                        'type': where.get('type', 1)})
        if mission == constants.Missions['RecycleDebrisField']:
            # planet type: 1
            # debris type: 2
            # moon type: 3
            payload.update({'type': 2})  # Send to debris field
        res = self.session.post(self.get_url('fleet3'), data=payload).content

        payload = {}
        payload.update(get_hidden_fields(res))
        payload.update({'crystal': resources.get('crystal'),
                        'deuterium': resources.get('deuterium'),
                        'metal': resources.get('metal'),
                        'mission': mission})
        res = self.session.post(self.get_url('movement'), data=payload).content

        res = self.session.get(self.get_url('movement')).content
        soup = BeautifulSoup(res, 'html.parser')
        origin_coords = soup.find('meta', {'name': 'ogame-planet-coordinates'})['content']
        fleets = soup.findAll('div', {'class': 'fleetDetails'})
        matches = []
        for fleet in fleets:
            origin = fleet.find('span', {'class': 'originCoords'}).text
            dest = fleet.find('span', {'class': 'destinationCoords'}).text
            reversal_span = fleet.find('span', {'class': 'reversal'})
            if not reversal_span:
                continue
            fleet_id = int(reversal_span.get('ref'))
            if dest == '[{}:{}:{}]'.format(where['galaxy'], where['system'],
                                           where['position']) and origin == '[{}]'.format(origin_coords):
                matches.append(fleet_id)
        if matches:
            return max(matches)
        return None

    def cancel_fleet(self, fleet_id):
        res = self.session.get(self.get_url('movement') + '&return={}'.format(fleet_id)).content
        if not self.is_logged(res):
            raise NOT_LOGGED

    def get_fleets(self):
        res = self.session.get(self.get_url('movement')).content
        if not self.is_logged(res):
            raise NOT_LOGGED
        fleets = []
        soup = BeautifulSoup(res, 'html.parser')
        divs = soup.findAll('div', {'class': 'fleetDetails'})
        for div in divs:
            originText = div.find('span', {'class': 'originCoords'}).find('a').text
            coords = re.search(r'\[(\d+):(\d+):(\d+)\]', originText)
            galaxy, system, position = coords.groups()
            origin = (int(galaxy), int(system), int(position))
            destText = div.find('span', {'class': 'destinationCoords'}).find('a').text
            coords = re.search(r'\[(\d+):(\d+):(\d+)\]', destText)
            galaxy, system, position = coords.groups()
            dest = (int(galaxy), int(system), int(position))
            reversal_id = None
            reversal_span = div.find('span', {'class': 'reversal'})
            if reversal_span:
                reversal_id = int(reversal_span.get('ref'))
            mission_type = int(div.get('data-mission-type'))
            return_flight = bool(div.get('data-return-flight'))
            arrival_time = int(div.get('data-arrival-time'))
            ogameTimestamp = int(soup.find('meta', {'name': 'ogame-timestamp'})['content'])
            secs = arrival_time - ogameTimestamp
            if secs < 0: secs = 0
            trs = div.find('table', {'class': 'fleetinfo'}).findAll('tr')
            metal = parse_int(trs[-3].findAll('td')[1].text.strip())
            crystal = parse_int(trs[-2].findAll('td')[1].text.strip())
            deuterium = parse_int(trs[-1].findAll('td')[1].text.strip())
            fleet = {
                'id': reversal_id,
                'origin': origin,
                'destination': dest,
                'mission': mission_type,
                'return_flight': return_flight,
                'arrive_in': secs,
                'resources': {
                    'metal': metal,
                    'crystal': crystal,
                    'deuterium': deuterium,
                },
                'ships': {
                    'light_fighter': 0,
                    'heavy_fighter': 0,
                    'cruiser': 0,
                    'battleship': 0,
                    'battlecruiser': 0,
                    'bomber': 0,
                    'destroyer': 0,
                    'deathstar': 0,
                    'small_cargo': 0,
                    'large_cargo': 0,
                    'colony_ship': 0,
                    'recycler': 0,
                    'espionage_probe': 0,
                    'solar_satellite': 0,
                }
            }
            for i in range(1, len(trs) - 5):
                name = trs[i].findAll('td')[0].text.strip(' \r\t\n:')
                short_name = ''.join(name.split())
                code = get_code(short_name)
                qty = parse_int(trs[i].findAll('td')[1].text.strip())
                if code == 202: fleet['ships']['small_cargo'] = qty
                if code == 203: fleet['ships']['large_cargo'] = qty
                if code == 204: fleet['ships']['light_fighter'] = qty
                if code == 205: fleet['ships']['heavy_fighter'] = qty
                if code == 206: fleet['ships']['cruiser'] = qty
                if code == 207: fleet['ships']['battleship'] = qty
                if code == 208: fleet['ships']['colony_ship'] = qty
                if code == 209: fleet['ships']['recycler'] = qty
                if code == 210: fleet['ships']['espionage_probe'] = qty
                if code == 211: fleet['ships']['bomber'] = qty
                if code == 212: fleet['ships']['solar_satellite'] = qty
                if code == 213: fleet['ships']['destroyer'] = qty
                if code == 214: fleet['ships']['deathstar'] = qty
                if code == 215: fleet['ships']['battlecruiser'] = qty
            fleets.append(fleet)
        return fleets

    def get_fleet_ids(self):
        """Return the reversable fleet ids."""
        res = self.session.get(self.get_url('movement')).content
        if not self.is_logged(res):
            raise NOT_LOGGED
        soup = BeautifulSoup(res, 'html.parser')
        spans = soup.findAll('span', {'class': 'reversal'})
        fleet_ids = [span.get('ref') for span in spans]
        return fleet_ids
