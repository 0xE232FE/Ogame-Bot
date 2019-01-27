import logging

from old_python.ogame_bot.actions.action import Action


class Military(Action):
    def __init__(self, bot, mode):
        super().__init__(bot, mode)

    def perform_action(self, planet):
        if self.bot.user.is_under_attack():
            logging.warning(f"{self.__class__.__name__}:: Is under attack !!")

        self.create_fleet()

    def create_fleet(self):
        pass

