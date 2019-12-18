from slackbot.bot import Bot
from slackbot.slackclient import SlackClient as client

from plugins import DMHandler as dm
import configparser
import sys
import schedule, time

sys.dont_write_bytecode = True


conf = configparser.ConfigParser()
conf.read('./config.ini')
API_TOKEN = conf['slack']['BOT_USER_OAUTH_ACCESS_TOKEN']


def main():
    cl = client(API_TOKEN)
    schedule.every().monday.at('10:00').do(dm.sendReminder4MinutesDuty, cl, 'b4')
    schedule.every().wednesday.at('18:00').do(dm.sendReminder4TrashDuty, cl)
    schedule.every().wednesday.at('10:00').do(dm.sendReminder4MinutesDuty, cl, 'm1')

    while True:
        schedule.run_pending()
        time.sleep(1)

    bot = Bot()
    bot.run()

if __name__ == '__main__':
    print('Start slackBot')
    main()
