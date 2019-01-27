from old_python.ogame_bot.actions.action import Action


class Economy(Action):
    def __init__(self, bot, mode):
        super().__init__(bot, mode)

    def perform_action(self, planet):
        planet_buildings = planet.get_planet_buildings()
