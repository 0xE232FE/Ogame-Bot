import argparse
import logging
import sys

from old_python import ogame_bot
from old_python.ogame_bot import Bot
from old_python.ogame_bot.config import load_config


def main(args=None):
    if not args:
        args = sys.argv[1:]

    parser = argparse.ArgumentParser(description='Bot')

    parser.add_argument('-u', '--username', help='Account username.', default=None)
    parser.add_argument('-s', '--servername', help='Account servername.', default=None)
    parser.add_argument('-p', '--password', help='Account password.', default=None)

    parser.add_argument('-m', '--mode', help='Bot mode.', default="StarterBuilderMode")

    args = parser.parse_args(args)

    logging.getLogger().setLevel(logging.INFO)
    logging.info("Bot is starting...")

    if not args.servername or not args.username or not args.password:
        config = load_config()
        if config:
            if not args.servername and "universe" in config:
                args.servername = config["universe"]
            if not args.username and "user" in config:
                args.username = config["user"]
            if not args.password and "password" in config:
                args.password = config["password"]
            if "mode" in config:
                args.mode = config["mode"]

    bot = Bot(args.servername, args.username, args.password)

    ogame_bot.__init__(bot)
    bot.connect()
    bot.initialize()
    bot.active_mode(args.mode)


if __name__ == '__main__':
    main()
