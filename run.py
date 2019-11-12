from flask import Flask, request, Response
from slackbot.bot import Bot
from werkzeug.wrappers import json

import slackbot_settings as conf

app = Flask(__name__)


@app.route('/', methods=['post'])
def verifyUrl():
    body = request.get_json()
    if body['token'] != conf.API_TOKEN:
        return Response(response=json.dumps({'message': 'Not Forbidden'}), status=403)
    if body['type'] == 'url_verification':
        return Response(response=body['challenge'], status=200)


def main():
    bot = Bot()
    bot.run()


if __name__ == '__main__':
    main()
