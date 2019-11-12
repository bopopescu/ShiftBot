import configparser
import json

from flask import Flask, request, Response, app
from slackbot.bot import respond_to, default_reply

conf = configparser.ConfigParser()
members = conf.read('./members.ini')

members_2525 = members["members"]["m2525"].split()
members_2721 = members["members"]["m2721"].split()

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
