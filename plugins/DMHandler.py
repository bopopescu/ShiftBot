from slackbot.slackclient import SlackClient as client

from plugins import Repository as repo
from logs import LogHandler as log

attempt = 'ULMK1UHJS'

def sendDMTest(token, text):
    sc = client(token)
    client.send_message(self=sc, channel=attempt, message=text)

def sendReminder4TrashDuty(token):
    sc = client(token)
    text = '明日のごみ捨て当番です. よろしくお願いします. '
    id2525 = repo.getSlackIDofTrashDuty('2525')
    id2721 = repo.getSlackIDofTrashDuty('2721')
    client.send_message(self=sc, channel=attempt, message=text)
    # client.send_message(self=sc, channel=id2525, message=text)
    # client.send_message(self=sc, channel=id2721, message=text)
    log.logInfo('Send message(' + text + ') to' + id2525 +' and ' + id2721)


def sendReminder4TodaysTrashDuty(token):
    sc = client(token)
    text = "本日のごみ捨て当番です．よろしくお願いします．"
    id2525 = repo.getSlackIDofTrashDuty('2525')
    id2721 = repo.getSlackIDofTrashDuty('2721')
    client.send_message(self=sc, channel=attempt, message=text)
    # client.send_message(self=sc, channel=id2525, message=text)
    # client.send_message(self=sc, channel=id2721, message=text)
    log.logInfo('Send message(' + text + ') to' + id2525 +' and ' + id2721)


def sendReminder4MinutesDuty(token, *grade):
    sc = client(token)
    text = '本日の議事録当番です. よろしくお願いします. '
    userid = repo.getSlackIDofMinutesDuty(grade)
    client.send_message(self=sc, channel=attempt, message=text)
    # client.send_message(self=sc, channel=userid, message=text)
    log.logInfo('Send message(' + text + ') to' + userid)
