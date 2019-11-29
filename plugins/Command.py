from plugins import Repository as repo
from slackbot.bot import respond_to


@respond_to('next trash -r 2525')
def nextTrash2525(message, args):
    repo.nextTrash('2525')
    message.reply(repo.presentTrash('2525'))


@respond_to('next trash -r 2721')
def nextTrash2525(message, args):
    repo.nextTrash('2721')
    message.reply(repo.presentTrash('2721'))


@respond_to('next minutes')
def nextTrash2525(message, args):
    repo.nextMinutes()
    message.reply(repo.presentMinutes())


@respond_to('prev trash -r 2525')
def prevTrash2525(message):
    repo.prevTrash('2525')
    message.reply(repo.presentTrash('2525'))


@respond_to('prev trash -r 2721')
def prevTrash2721(message):
    repo.prevTrash('2721')
    message.reply(repo.presentTrash('2721'))

