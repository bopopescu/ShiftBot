from plugins import Repository as repo
from slackbot.bot import respond_to, default_reply


@respond_to('hare next trash 2525')
def nextTrash2525(message, args):
    repo.nextTrash('2525')
    message.reply(repo.presentTrash('2525'))


@respond_to('hare next trash 2721')
def nextTrash2525(message, args):
    repo.nextTrash('2721')
    message.reply(repo.presentTrash('2721'))


@respond_to('hare next minutes')
def nextTrash2525(message, args):
    repo.nextMinutes()
    message.reply(repo.presentMinutes())
