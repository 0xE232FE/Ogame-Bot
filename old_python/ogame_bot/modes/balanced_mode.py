import logging

from old_python.ogame_bot import Attacker
from old_python.ogame_bot import Defender
from old_python.ogame_bot.actions.economy import Economy
from old_python.ogame_bot.actions.military import Military
from old_python.ogame_bot import Researcher
from old_python.ogame_bot.modes.mode import Mode


class BalancedMode(Mode):
    def __init__(self, bot, session):
        super().__init__(bot, session)

        logging.info(f"{self.__class__.__name__}:: starting...")

        self.action_matrix = {
            Economy.__name__: Economy(self.bot, self).start(),
            Researcher.__name__: Researcher(self.bot, self).start(),
            Attacker.__name__: Attacker(self.bot, self).start(),
            Defender.__name__: Defender(self.bot, self).start(),
            Military.__name__: Military(self.bot, self).start()
        }

    def run(self):
        pass

    def stop(self):
        for action in self.action_matrix.values():
            action.stop()
