import json

from flask import Flask, request, Response, app
from slackbot.bot import respond_to, default_reply


members_2525 = ['陳', '伊藤', '庵谷', '勝又', '斎藤', '佐藤', '鈴木', '中野', '永野']
members_2721 = ['村田', '清水', '若月', '梅田', '誓山']
count = 0


@app.route('/')
def hello_world():
    return 'Hello World!'


@respond_to('議事録')
def replayMinutesTaker(message, name):
    message.replay('次回の議事録当番は{}さんです。'.format(name))


@respond_to(r'ごみ|ゴミ|trash|garbage')
def replayTrashTaker(message, name):
    message.replay('次回のゴミ捨て当番は{}さんです.'.format(name))


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
