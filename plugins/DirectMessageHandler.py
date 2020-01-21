from slackbot.slackclient import SlackClient as client

from plugins import Repository as repo
from plugins.CircularLinkedListRepository import CircularLinkedListRepository
from logs import LogHandler as log

import configparser

class DirectMessageHandler:
    conf = configparser.ConfigParser()
    conf.read('./config.ini')
    API_TOKEN = conf['slack']['BOT_USER_OAUTH_ACCESS_TOKEN']

    attempt = 'ULMK1UHJS'

    def sendDMTest(self, text, target):
        # sc = client(API_TOKEN)
        # client.send_message(self=sc, channel=attempt, message=text)
        print("Send msg'%s' to %s" % (text, target))
    
    def sendDM(self, text, target):
        sc = client(API_TOKEN)
        client.send_message(self=sc, channel=target, message=text)
