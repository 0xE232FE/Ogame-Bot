import json
import re

from bs4 import BeautifulSoup

from lib.ogame import NOT_LOGGED, parse_int, get_planet_infos_regex


class Galaxy:
    def __init__(self, bot):
        self.bot = bot

    def get_planet_infos(self, planet_id, res=None):
        if not res:
            res = self.bot.session.get(self.bot.get_url('overview', {'cp': planet_id})).content
        self.bot.is_logged(res)
        soup = BeautifulSoup(res, 'html.parser')
        link = soup.find('div', {'id': 'planet-{}'.format(planet_id)})
        if link is not None:  # is a planet pid
            link = link.find('a')
        else:  # is a moon pid
            link = soup.find('div', {'id': 'planetList'})
            link = link.find_all('a', {'class': 'moonlink'})
            for node in link:
                nodeContent = node['title']
                if nodeContent.find("cp=" + planet_id) > -1:
                    link = node
                    break
                else:
                    continue

        infos_label = BeautifulSoup(link['title'], 'html.parser').text
        infos = get_planet_infos_regex(infos_label)
        res = {'img': link.find('img').get('src'), 'id': planet_id, 'planet_name': infos.group(1),
               'diameter': parse_int(infos.group(5)),
               'coordinate': {
                   'galaxy': int(infos.group(2)),
                   'system': int(infos.group(3)),
                   'position': int(infos.group(4))
               },
               'fields': {'built': int(infos.group(6)),
                          'total': int(infos.group(7))},
               'temperature': {}}

        if infos.groups().__len__() > 7:  # is a planet
            res['temperature']['min'] = int(infos.group(8))
            res['temperature']['max'] = int(infos.group(9))
        return res

    def galaxy_content(self, galaxy, system):
        headers = {'X-Requested-With': 'XMLHttpRequest',
                   'Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8'}
        payload = {'galaxy': galaxy, 'system': system}
        url = self.bot.get_url('galaxyContent', {'ajax': 1})
        res = self.bot.session.post(url, data=payload, headers=headers).content.decode('utf8')
        try:
            obj = json.loads(res)
        except ValueError:
            raise NOT_LOGGED
        return obj

    def galaxy_infos(self, galaxy, system):
        html = self.galaxy_content(galaxy, system)['galaxy']
        soup = BeautifulSoup(html, 'html.parser')
        rows = soup.findAll('tr', {'class': 'row'})
        res = []
        for row in rows:
            if 'empty_filter' not in row.get('class'):
                activity = None
                activity_div = row.findAll('div', {'class': 'activity'})
                if len(activity_div) > 0:
                    activity_raw = activity_div[0].text.strip()
                    if activity_raw != '':
                        activity = int(activity_raw)
                    else:
                        activity = 0
                tooltips = row.findAll('div', {'class': 'htmlTooltip'})
                planet_tooltip = tooltips[0]
                planet_name = planet_tooltip.find('h1').find('span').text
                planet_url = planet_tooltip.find('img').get('src')
                coords_raw = planet_tooltip.find('span', {'id': 'pos-planet'}).text
                coords = re.search(r'\[(\d+):(\d+):(\d+)\]', coords_raw)
                galaxy, system, position = coords.groups()
                planet_infos = {'activity': activity,
                                'name': planet_name,
                                'img': planet_url,
                                'coordinate': {
                                    'galaxy': int(galaxy),
                                    'system': int(system),
                                    'position': int(position)}
                                }
                if len(tooltips) > 2:
                    for i in range(1, 3):
                        player_tooltip = tooltips[i]
                        player_id_raw = player_tooltip.get('id')
                        if player_id_raw.startswith('debris'):
                            continue
                        player_id = int(re.search(r'player(\d+)', player_id_raw).groups()[0])
                        player_name = player_tooltip.find('h1').find('span').text
                        player_rank = parse_int(player_tooltip.find('li', {'class': 'rank'}).find('a').text)
                        break
                elif len(tooltips) > 1:
                    player_tooltip = tooltips[1]
                    player_id_raw = player_tooltip.get('id')
                    player_id = int(re.search(r'player(\d+)', player_id_raw).groups()[0])
                    player_name = player_tooltip.find('h1').find('span').text
                    player_rank = parse_int(player_tooltip.find('li', {'class': 'rank'}).find('a').text)
                else:
                    player_id = None
                    player_name = row.find('td', {'class': 'playername'}).find('span').text.strip()
                    player_rank = None
                planet_infos['player'] = {
                    'id': player_id,
                    'name': player_name,
                    'rank': player_rank
                }
                res.append(planet_infos)
        return res
