from flask import Flask
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

def main():
    bot = Bot()
    bot.run()


def sendingSchedule():
    # schedule.every().thursday.at('11:00').do(dm.sendReminder4TodaysTrashDuty, API_TOKEN)
    schedule.every(6).hours.do(repo.ping)
    # schedule.every().monday.at('18:30').do(dm.sendReminder4MinutesDuty, 'm1')
    # schedule.every().wednesday.at('18:30').do(dm.sendReminder4MinutesDuty, 'b4')
    schedule.every(10).seconds.do(dm.minutesTest)

    i = 0
    while True:
        schedule.run_pending()
        print(i)
        i += 1
        time.sleep(1)


if __name__ == '__main__':
    print('Start slackBot')
    multiprocessing.Process(target=main).start()
    multiprocessing.Process(target=sendingSchedule).start()
