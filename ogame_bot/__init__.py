import random

from lib.ogame import CANT_PROCESS, NOT_LOGGED

bot_instance = None


def __init__(bot):
    global bot_instance
    bot_instance = bot


def get_bot():
    return bot_instance


def retry_if_logged_out(method):
    def wrapper(self, *args, **kwargs):
        attempt = 0
        succeed = False
        res = None
        while not succeed:
            try:
                res = method(self, *args, **kwargs)
                succeed = True
            except NOT_LOGGED:
                random.randint(2, 60)
                attempt += 1
                if attempt > 5:
                    raise CANT_PROCESS
                succeed = False
                bot_instance.connect()
        return res

    return wrapper
