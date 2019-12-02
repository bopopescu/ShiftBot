# coding: utf-8
from slackbot.bot import respond_to

from plugins import Repository as repo


@respond_to(r'^(?=.*(ごみ|ゴミ))(?!.*(2525|2721)).*$')
def sendTrashDuty2525AND2721(message, args):
    sendTrashDutyIn2525(message, args)
    sendTrashDutyIn2721(message, args)


@respond_to(r'^(?=.*(ごみ|ゴミ|trash|garbage))(?=.*2525)')
def sendTrashDutyIn2525(message, args):
    name = repo.presentTrash('2525')
    message.send('2525室の次回のごみ捨て当番は%sさんです。' % name)


@respond_to(r'^(?=.*(ごみ|ゴミ|trash|garbage))(?=.*2721)')
def sendTrashDutyIn2721(message, args):
    name = repo.presentTrash('2721')
    message.send('2721室の次回のごみ捨て当番は%sさんです。' % name)


@respond_to(r'(議事録|議事)')
def sendMinutesTaker(message, args):
    name = repo.presentMinutes()
    message.send('次回の議事録当番は%sさんです。' % name)


@respond_to(r'^(?=.*(ごみ|ゴミ))(?=.*終)')
def sendNextTrashDuty(message, args):
    name2525 = repo.nextTrash('2525')
    name2721 = repo.nextTrash('2721')
    message.send('''ありがとうございます。次回のごみ捨て当番は\n2525室：%sさん\n2721室：%sさん\nです。よろしくお願いします。''' % (name2525, name2721))


def sendNextMinutesDuty(message, args):
    name = repo.nextMinutes()
    message.send('''定例ミーティングお疲れさまです。\n
                    次回の議事録当番は%sさんです。よろしくお願いします。''' % name)


def sendTodaysMinutesDuty(message, args):
    name = repo.presentMinutes()
    message.send('本日の議事録当番は%sさんです。よろしくお願いします。' % name)
