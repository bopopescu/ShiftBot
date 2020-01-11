from slackbot.bot import Bot
from slackbot.slackclient import SlackClient as client

from plugins import DMHandler as dm
from plugins import Repository as repo
import configparser
import sys
import schedule
import time
import multiprocessing

sys.dont_write_bytecode = True
conf = configparser.ConfigParser()
conf.read('./config.ini')
API_TOKEN = conf['slack']['BOT_USER_OAUTH_ACCESS_TOKEN']


def main():
    bot = Bot()
    bot.run()


def sendingSchedule():
    # schedule.every().monday.at('10:00').do(dm.sendReminder4MinutesDuty, API_TOKEN, 'b4')
    # schedule.every().thursday.at('11:00').do(dm.sendReminder4TodaysTrashDuty, API_TOKEN)
    # schedule.every().wednesday.at('10:00').do(dm.sendReminder4MinutesDuty, API_TOKEN, 'm1')
    schedule.every().hour(6).do(repo.ping)
    while True:
        schedule.run_pending()
        time.sleep(1)


if __name__ == '__main__':
    print('Start slackBot')
    multiprocessing.Process(target=main).start()
    # multiprocessing.Process(target=sendingSchedule).start()
