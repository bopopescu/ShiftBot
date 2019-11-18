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


@respond_to('議事録')
def replayMinutesTaker(message):
    return None


@respond_to(r'ごみ|ゴミ|trash|garbage')
def replayTrashTaker(message, room):
    return None

# def whoIsOnMinutesDuty():


@respond_to(r'(ごみ|ゴミ|trash|garbage)')
def replayTrashDutyIn2525(room):
    repo.presentTrash('2525')


def replayTrashDutyIn2721():
    repo.presentTrash('2721')


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
