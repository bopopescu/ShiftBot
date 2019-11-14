import configparser

from plugins import Cycle

from flask import app
from slackbot.bot import respond_to, default_reply

conf = configparser.ConfigParser()
members = conf.read('./members.ini')


#####################################
# あんまりよろしくない気がする
#####################################

members_2525 = Cycle(members['members']['m2525'].split())
members_2721 = Cycle(members['members']['m2721'].split())
members_giji = Cycle(members['members']['giji'].split())

count = 0
giji_duty = 0
trash_duty_2525 = 0
trash_duty_2721 = 0


@app.route('/')
def hello_world():
    return 'Hello World!'


@respond_to('議事録')
def replayMinutesTaker(message):
    message.replay('次回の議事録当番は{}さんです。'.format(whoIsOnMinutesDuty()))


@respond_to(r'ごみ|ゴミ|trash|garbage')
def replayTrashTaker(message, room):
    if room == '2525':
        message.replay('次回のゴミ捨て当番は{}さんです.'.format(whoIsOnTrashDutyIn2525()))
    elif room == '2721':
        message.replay('次回のゴミ捨て当番は{}さんです.'.format(whoIsOnTrashDutyIn2721()))


#####################################
# cycleとかいうクソださ変数名何とかして.
# 一つにできん?
#####################################

def whoIsOnMinutesDuty():
    global giji_duty
    return members_giji.present()


def whoIsOnTrashDutyIn2525():
    global trash_duty_2525
    return members_2525.present()


def whoIsOnTrashDutyIn2721():
    global trash_duty_2721
    return members_2721.present()


@respond_to(r'^(?=.*[ごみ|ゴミ|trash|garbage])(?=.*[終|done])(?=2525).*$')
def whosNext():
    # if 当番完了の合図があったら
    nextDuty = members_2525.next()
    replayTrashTaker('2525')
    return nextDuty


@respond_to(r'^(?=.*[議事録])(?=.*[終|done]).*$')
def whosNextMinutes():
    # if 当番完了の合図があったら
    nextDuty = members_2525.next()
    replayMinutesTaker()
    return nextDuty


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
