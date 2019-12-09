from flask import Flask, request, Response
from slackbot.bot import Bot
import configparser
import json
import sys

sys.dont_write_bytecode = True

app = Flask(__name__)

conf = configparser.ConfigParser()
conf.read('./config.ini')
VERIFICATION_TOKEN = conf['slack']['verification_token']


@app.route('/')
def helloWorld():
    return 'This is slack bot for Lab.'


@app.route('/', methods=['post'])
def verifyUrl():
    body = request.get_json()
    if body['token'] != VERIFICATION_TOKEN:
        return Response(response=json.dumps({'message': 'Not Forbidden'}), status=403)
    elif body['type'] == 'url_verification':
        return Response(response=body['challenge'], status=200, headers='Content-Type: text/plain')


def main():
    bot = Bot()
    bot.run()


if __name__ == '__main__':
    print('Start slackBot')
    main()
