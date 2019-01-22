import argparse
import sys

from bot.bot import Bot


def main(args=None):
    if not args:
        args = sys.argv[1:]

    parser = argparse.ArgumentParser(description='Bot')
    parser.add_argument('-u', '--username', help='Account username.')
    parser.add_argument('-s', '--servername', help='Account servername.')
    parser.add_argument('-p', '--password', help='Account password.')

    args = parser.parse_args(args)

    bot = Bot(args.servername, args.username, args.password)
    bot.connect()


if __name__ == '__main__':
    main()
