import threading
from abc import ABCMeta


class Mode(threading.Thread):
    __metaclass__ = ABCMeta

    def __init__(self, bot, session):
        super().__init__()
        self.bot = bot
        self.session = session
        self.should_stop = False

        self.start()

    def run(self):
        raise NotImplementedError("run not implemented")
