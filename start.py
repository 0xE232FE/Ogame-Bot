import argparse
import logging
import sys

from bot.bot import Bot


def main(args=None):
    if not args:
        args = sys.argv[1:]

    parser = argparse.ArgumentParser(description='Bot')

    parser.add_argument('-u', '--username', help='Account username.')
    parser.add_argument('-s', '--servername', help='Account servername.')
    parser.add_argument('-p', '--password', help='Account password.')

    parser.add_argument('-m', '--mode', help='Bot mode.')

    args = parser.parse_args(args)

    logging.getLogger().setLevel(logging.INFO)
    logging.info("Bot is starting...")
    bot = Bot(args.servername, args.username, args.password)
    bot.connect()
    bot.active_mode(args.mode)


if __name__ == '__main__':
    main()
