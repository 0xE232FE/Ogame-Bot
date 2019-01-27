from ogame_bot.actions.action import Action


class Defender(Action):
    def __init__(self, bot, mode):
        super().__init__(bot, mode)

    def perform_action(self, planet):
        # planet_defenses = planet.get_defense()
        # NOTHING ELSE BECAUSE DEFENDING IS FOR PU**Y
        pass
