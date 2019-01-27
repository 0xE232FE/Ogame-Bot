import logging

from bs4 import BeautifulSoup

from ogame_bot import get_bot
from ogame_bot.lib.ogame import parse_int, metal_mine_production


class Game:
    def __init__(self):
        self.bot = get_bot()

    def get_universe_speed(self, res=None):
        if not res:
            res = self.bot.wrapper.session.get(self.bot.get_url('techtree', {'tab': 2, 'techID': 1})).content
        soup = BeautifulSoup(res, 'html.parser')
        if soup.find('head'):
            logging.warning(f"{self.__class__.__name__}:: Disconnected...")
        spans = soup.findAll('span', {'class': 'undermark'})
        level = parse_int(spans[0].text)
        val = parse_int(spans[1].text)
        metal_production = metal_mine_production(level, 1)
        universe_speed = val / metal_production
        return universe_speed
