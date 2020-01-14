from slackbot.slackclient import SlackClient as client

from plugins import Repository as repo
from plugins.CircularLinkedListRepository import CircularLinkedListRepository
from logs import LogHandler as log

import configparser

conf = configparser.ConfigParser()
conf.read('./config.ini')
API_TOKEN = conf['slack']['BOT_USER_OAUTH_ACCESS_TOKEN']

attempt = 'ULMK1UHJS'

rp = CircularLinkedListRepository()

def sendDMTest(text):
    # sc = client(API_TOKEN)
    # client.send_message(self=sc, channel=attempt, message=text)
    print(text)

def sendReminder4TrashDuty():
    sc = client(API_TOKEN)
    text = '明日のごみ捨て当番です. よろしくお願いします. '
    id2525 = repo.getSlackIDofTrashDuty('2525')
    id2721 = repo.getSlackIDofTrashDuty('2721')
    client.send_message(self=sc, channel=attempt, message=text)
    # client.send_message(self=sc, channel=id2525, message=text)
    # client.send_message(self=sc, channel=id2721, message=text)
    log.logInfo('Send message(' + text + ') to' + id2525 +' and ' + id2721)


def sendReminder4TodaysTrashDuty():
    sc = client(API_TOKEN)
    text = "本日のごみ捨て当番です．よろしくお願いします．"
    id2525 = repo.getSlackIDofTrashDuty('2525')
    id2721 = repo.getSlackIDofTrashDuty('2721')
    client.send_message(self=sc, channel=attempt, message=text)
    # client.send_message(self=sc, channel=id2525, message=text)
    # client.send_message(self=sc, channel=id2721, message=text)
    log.logInfo('Send message(' + text + ') to' + id2525 +' and ' + id2721)


def sendReminder4MinutesDuty(nextGrade):
    sc = client(API_TOKEN)
    text = '次回の議事録当番です. よろしくお願いします. '
    userid = rp.nextMinutes(nextGrade)
    print(userid)
    # client.send_message(self=sc, channel=attempt, message=text)
    # client.send_message(self=sc, channel=userid, message=text)
    log.logInfo('Send message(' + text + ') to' + userid)

def minutesTest():
    sc = client(API_TOKEN)
    text = '次回の議事録当番です. よろしくお願いします. '
    name1 = rp.nextMinutes('m1')
    name2 = rp.nextMinutes('b4')
    print(name1)
    print(name2)
    # client.send_message(self=sc, channel=attempt, message=text)
    # client.send_message(self=sc, channel=userid, message=text)
