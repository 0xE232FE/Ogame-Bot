import datetime
import json
import math
import re
import time
import arrow
import requests
import random

from . import constants
from .errors import BAD_UNIVERSE_NAME, BAD_DEFENSE_ID, NOT_LOGGED, BAD_CREDENTIALS, CANT_PROCESS, BAD_BUILDING_ID, \
    BAD_SHIP_ID, BAD_RESEARCH_ID
from bs4 import BeautifulSoup
from dateutil import tz

from lib.ogame.constants import Calculate


def parse_int(text):
    return int(text.replace('.', '').replace(',', '').strip())


def for_all_methods(decorator):
    def decorate(cls):
        for attr in cls.__dict__:  # there's propably a better way to do this
            if callable(getattr(cls, attr)):
                setattr(cls, attr, retry_if_logged_out(decorator(getattr(cls, attr))))
        return cls

    return decorate


def sandbox_decorator(some_fn):
    def wrapper(ogame, *args, **kwargs):
        fn_name = some_fn.__name__

        local_fns = ['get_datetime_from_time']

        if fn_name in local_fns:
            return some_fn(ogame, *args, **kwargs)

        if fn_name == '__init__' or not ogame.sandbox:
            return some_fn(ogame, *args, **kwargs)

        if fn_name in ogame.sandbox_obj:
            return ogame.sandbox_obj[fn_name]

        return None

    return wrapper


def retry_if_logged_out(method):
    def wrapper(self, *args, **kwargs):
        attempt = 0
        time_to_sleep = 0
        working = False
        while not working:
            try:
                working = True
                res = method(self, *args, **kwargs)
            except NOT_LOGGED:
                time.sleep(time_to_sleep)
                attempt += 1
                time_to_sleep += 1
                if attempt > 5:
                    raise CANT_PROCESS
                working = False
                self.login()
        return res

    return wrapper


def get_nbr(soup, name):
    div = soup.find('div', {'class': name})
    level = div.find('span', {'class': 'level'})
    for tag in level.findAll(True):
        tag.extract()
    return parse_int(level.text)


def metal_mine_production(level, universe_speed=1):
    return int(math.floor(30 * level * 1.1 ** level) * universe_speed)


def get_planet_infos_regex(text):
    result = re.search(r'(\w+) \[(\d+):(\d+):(\d+)\]([\d\.]+)km \((\d+)/(\d+)\)([-\d]+).+C (?:bis|to|à) ([-\d]+).+C',
                       text)
    if result is not None:
        return result  # is a plenet
    else:
        return re.search(r'(\w+) \[(\d+):(\d+):(\d+)\]([\d\.]+)km \((\d+)/(\d+)\)', text)  # is a moon


def get_code(name):
    if name in constants.Buildings.keys():
        return constants.Buildings[name]
    if name in constants.Facilities.keys():
        return constants.Facilities[name]
    if name in constants.Defense.keys():
        return constants.Defense[name]
    if name in constants.Ships.keys():
        return constants.Ships[name]
    if name in constants.Research.keys():
        return constants.Research[name]
    print('Couldn\'t find code for {}'.format(name))
    return None


@for_all_methods(sandbox_decorator)
class OGame(object):
    TIME_SLEEP_MAX = 2

    def __init__(self, universe, username, password, domain='fr.ogame.gameforge.com', auto_bootstrap=True,
                 sandbox=False, sandbox_obj=None):
        self.session = requests.session()
        self.session.headers.update(
            {'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64; rv:45.0) Gecko/20100101 Firefox/45.0'})
        self.sandbox = sandbox
        self.sandbox_obj = sandbox_obj if sandbox_obj is not None else {}
        self.universe = universe
        self.domain = domain
        self.username = username
        self.password = password
        self.universe_speed = 1
        self.server_url = ''
        self.server_tz = 'GMT+1'
        if auto_bootstrap:
            self.login()
            self.universe_speed = self.get_universe_speed()

    def login(self):
        """Get the ogame session token."""
        payload = {'kid': '',
                   'language': 'fr',
                   'autologin': 'false',
                   'credentials[email]': self.username,
                   'credentials[password]': self.password}
        time.sleep(random.uniform(1, self.TIME_SLEEP_MAX))
        res = self.session.post('https://lobby-api.ogame.gameforge.com/users', data=payload)

        php_session_id = None
        for c in res.cookies:
            if c.name == 'PHPSESSID':
                php_session_id = c.value
                break
        cookie = {'PHPSESSID': php_session_id}

        res = self.session.get('https://lobby-api.ogame.gameforge.com/servers').json()
        server_num = None
        for server in res:
            name = server['name'].lower()
            if self.universe.lower() == name:
                server_num = server['number']
                break

        res = self.session.get('https://lobby-api.ogame.gameforge.com/users/me/accounts', cookies=cookie)
        selected_server_id = None
        lang = None
        server_accounts = res.json()
        for server_account in server_accounts:
            if server_account['server']['number'] == server_num:
                lang = server_account['server']['language']
                selected_server_id = server_account['id']
                break

        time.sleep(random.uniform(1, self.TIME_SLEEP_MAX))
        res = self.session.get(
            'https://lobby-api.ogame.gameforge.com/users/me/loginLink?id={}&server[language]={}&server[number]={}'
                .format(selected_server_id, lang, str(server_num)), cookies=cookie).json()
        selected_server_url = res['url']
        b = re.search('https://(.+\.ogame\.gameforge\.com)/game', selected_server_url)
        self.server_url = b.group(1)

        res = self.session.get(selected_server_url).content
        soup = BeautifulSoup(res, 'html.parser')
        session_found = soup.find('meta', {'name': 'ogame-session'})
        if session_found:
            self.ogame_session = session_found.get('content')
        else:
            raise BAD_CREDENTIALS

    def logout(self):
        self.session.get(self.get_url('logout'))

    def is_logged(self, html=None):
        if not html:
            html = self.session.get(self.get_url('overview')).content
        soup = BeautifulSoup(html, 'html.parser')
        session = soup.find('meta', {'name': 'ogame-session'})
        return session is not None

    def get_page_content(self, page='overview', cp=None):
        """Return the html of a specific page."""
        payload = {}
        if cp is not None:
            payload.update({'cp': cp})
        html = self.session.get(self.get_url(page, payload)).content
        if not self.is_logged(html):
            raise NOT_LOGGED
        return html

    def fetch_eventbox(self):
        res = self.session.get(self.get_url('fetchEventbox')).content.decode('utf8')
        try:
            obj = json.loads(res)
        except ValueError:
            raise NOT_LOGGED
        return obj

    def get_datetime_from_time(self, hour, minute, second):
        attack_time = arrow.utcnow().to(self.server_tz).replace(hour=hour, minute=minute, second=second)
        now = arrow.utcnow().to(self.server_tz)
        if now.hour > attack_time.hour:
            attack_time += datetime.timedelta(days=1)
        return attack_time.to(tz.tzlocal()).datetime

    def get_url(self, page, params=None):
        if params is None:
            params = {}
        if page == 'login':
            return 'https://{}/main/login'.format(self.domain)
        else:
            if self.server_url == '':
                self.server_url = self.get_universe_url(self.universe)
            url = 'https://{}/game/index.php?page={}'.format(self.server_url, page)
            if params:
                arr = []
                for key in params:
                    arr.append("{}={}".format(key, params[key]))
                url += '&' + '&'.join(arr)
            return url

    def get_servers(self, domain):
        res = self.session.get('https://lobby-api.ogame.gameforge.com/servers').json()
        servers = {}
        for server in res:
            name = server['name'].lower()
            lang = server['language']
            num = server['number']
            url = 's{}-{}.ogame.gameforge.com'.format(num, lang)
            servers[name] = url
        return servers

    def get_universe_url(self, universe):
        """Get a universe name and return the server url."""
        servers = self.get_servers(self.domain)
        universe = universe.lower()
        if universe not in servers:
            raise BAD_UNIVERSE_NAME
        return servers[universe]

    def get_server_time(self):
        """Get the ogame server time."""
        res = self.session.get(self.get_url('overview')).content
        if not self.is_logged(res):
            raise NOT_LOGGED
        soup = BeautifulSoup(res, 'html.parser')
        date_str = soup.find('li', {'class': 'OGameClock'}).text
        date_format = '%d.%m.%Y %H:%M:%S'
        date = datetime.datetime.strptime(date_str, date_format)
        return date

    def get_ogame_version(self, res=None):
        """Get ogame version on your server."""
        if not res:
            res = self.session.get(self.get_url('overview')).content
        if not self.is_logged(res):
            raise NOT_LOGGED
        soup = BeautifulSoup(res, 'html.parser')
        footer = soup.find('div', {'id': 'siteFooter'})
        version = footer.find('a').text.strip()
        return version

    def get_overview(self, planet_id):
        html = self.session.get(self.get_url('overview', {'cp': planet_id})).content
        if not self.is_logged(html):
            raise NOT_LOGGED
        soup = BeautifulSoup(html, 'html.parser')
        boxes = soup.findAll('div', {'class': 'content-box-s'})
        res = {}
        names = ['buildings', 'research', 'shipyard']
        for idx, box in enumerate(boxes):
            is_idle = box.find('td', {'class': 'idle'}) is not None
            res[names[idx]] = []
            if not is_idle:
                name = box.find('th').text
                short_name = ''.join(name.split())
                code = get_code(short_name)
                desc = box.find('td', {'class': 'desc'}).text
                desc = ' '.join(desc.split())
                tmp = [{'name': short_name, 'code': code}]
                if idx == 2:
                    quantity = parse_int(box.find('div', {'id': 'shipSumCount7'}).text)
                    tmp[0].update({'quantity': quantity})
                    queue = box.find('table', {'class': 'queue'})
                    if queue:
                        tds = queue.findAll('td')
                        for td_element in tds:
                            link = td_element.find('a')
                            quantity = parse_int(link.text)
                            img = td_element.find('img')
                            alt = img['alt']
                            short_name = ''.join(alt.split())
                            code = get_code(short_name)
                            tmp.append({'name': short_name, 'code': code, 'quantity': quantity})
                res[names[idx]] = tmp
        return res
