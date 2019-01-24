from bs4 import BeautifulSoup

from lib.ogame import NOT_LOGGED, parse_int, metal_mine_production


class Game:
    def __init__(self, bot):
        self.bot = bot

    def get_universe_speed(self, res=None):
        if not res:
            res = self.bot.wrapper.session.get(self.bot.get_url('techtree', {'tab': 2, 'techID': 1})).content
        soup = BeautifulSoup(res, 'html.parser')
        if soup.find('head'):
            raise NOT_LOGGED
        spans = soup.findAll('span', {'class': 'undermark'})
        level = parse_int(spans[0].text)
        val = parse_int(spans[1].text)
        metal_production = metal_mine_production(level, 1)
        universe_speed = val / metal_production
        return universe_speed
