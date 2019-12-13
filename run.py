from slackbot.bot import Bot
import configparser
import sys

sys.dont_write_bytecode = True


conf = configparser.ConfigParser()
conf.read('./config.ini')
VERIFICATION_TOKEN = conf['slack']['verification_token']


def main():
    bot = Bot()
    bot.run()


if __name__ == '__main__':
    print('Start slackBot')
    main()
