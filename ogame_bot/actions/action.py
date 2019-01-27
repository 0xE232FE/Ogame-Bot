from abc import ABCMeta, abstractmethod


class Action:
    __metaclass__ = ABCMeta

    def __init__(self, bot):
        self.bot = bot

    @abstractmethod
    def evaluate(self):
        raise NotImplementedError("evaluate not implemented")
