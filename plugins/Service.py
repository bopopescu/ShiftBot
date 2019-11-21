from flask import app
from slackbot.bot import respond_to, default_reply

from plugins import Repository as repo


count = 0
giji_duty = 0
trash_duty_2525 = 0
trash_duty_2721 = 0


@app.route('/')
def hello_world():
    return 'Hello World!'


@respond_to(r'(ごみ|ゴミ|trash|garbage)')
def sendTrashDutyIn2525(message):
    name = repo.presentTrash('2525')
    message.send('2525室の次回のごみ捨て当番は%sさんです。', name)


@respond_to(r'(ごみ|ゴミ|trash|garbage)')
def sendTrashDutyIn2721(message):
    name = repo.presentTrash('2721')
    message.send('2721室の次回のごみ捨て当番は%sさんです。', name)


@respond_to(r'(議事録|議事)')
def sendMinutesTaker(message):
    name = repo.presentMinutes()
    message.send('次回の議事録当番は%sさんです。', name)


def sendNextTrashDuty(message):
    name2525 = repo.nextTrash('2525')
    name2721 = repo.nextTrash('2721')
    message.send('''次回のごみ捨て当番は\n
                    2525室：%sさん\n
                    2721室：%sさん\n
                    です。よろしくお願いします。''', name2525, name2721)


def sendNextMinutesDuty(message):
    name = repo.nextMinutes()
    message.send('''定例ミーティングお疲れさまです。\n
                    次回の議事録当番は%sさんです。よろしくお願いします。''', name)


def sendTodaysMinutesDuty(message):
    name = repo.presentMinutes()
    message.send('本日の議事録当番は%sさんです。よろしくお願いします。', name)


# @respond_to(r'^(?=.*[ごみ|ゴミ|trash|garbage])(?=.*[終|done])(?=2525).*$')
# def whosNext():


# @respond_to(r'^(?=.*[議事録])(?=.*[終|done]).*$')
# def whosNextMinutes():


@default_reply()
def easterEgg(message):
    global count
    count += 1
    if count % 500 == 0 and count < 1000:
        message.replay('{}回目の意味のないメッセージを受信しました！この調子です！！！' % count)
        message.react('+1')
    elif count % 100 == 0 and count < 1000:
        message.replay('{}回目の意味のないメッセージを受信しました！おめでとうございます！！！' % count)
        message.react('+1')
    elif count == 1000:
        message.replay('{}回目の意味のないメッセージを受信しました！私の完敗です...！！！' % count)
        message.replay('これ以上は何もありません！！！')
        message.react('+1')
