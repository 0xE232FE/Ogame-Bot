import logging

from ogame_bot.actions.action import Action


class FleetManager(Action):
    def __init__(self, bot, mode):
        super().__init__(bot, mode)

    def perform_action(self, planet):
        ships = planet.planet_ships.get_ships()
        military_ships = planet.planet_ships.get_military_ships(without_cargo=False, ships=ships)
        civilian_ships = planet.planet_ships.get_civilian_ships(with_probe=True, ships=ships)

        if self.bot.user.is_under_attack():
            logging.warning(f"{self.__class__.__name__}:: Is under attack !!")
