from ogame_bot.actions.action import Action


class Attacker(Action):
    def __init__(self, bot, mode):
        super().__init__(bot, mode)

    def perform_action(self, planet):
        pass
