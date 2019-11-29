# coding: utf-8
from slackbot.bot import respond_to, default_reply

from plugins import Repository as repo


@respond_to(r'^(?=.*(ごみ|ゴミ|trash|garbage))(?=.*2525)')
def sendTrashDutyIn2525(message, args):
    print(args)
    name = repo.presentTrash('2525')
    message.send('2525室の次回のごみ捨て当番は%sさんです。' % name)


@respond_to(r'^(?=.*(ごみ|ゴミ|trash|garbage))(?=.*2721)')
def sendTrashDutyIn2721(message, args):
    name = repo.presentTrash('2721')
    message.send('2721室の次回のごみ捨て当番は%sさんです。' % name)


@respond_to(r'(議事録|議事)')
def sendMinutesTaker(message, args):
    name = repo.presentMinutes()
    print(name+'さん')
    message.send('次回の議事録当番は%sさんです。' % name)


def sendNextTrashDuty(message, args):
    name2525 = repo.nextTrash('2525')
    name2721 = repo.nextTrash('2721')
    message.send('''次回のごみ捨て当番は\n
                    2525室：%sさん\n
                    2721室：%sさん\n
                    です。よろしくお願いします。''' % (name2525, name2721))


def sendNextMinutesDuty(message, args):
    name = repo.nextMinutes()
    message.send('''定例ミーティングお疲れさまです。\n
                    次回の議事録当番は%sさんです。よろしくお願いします。''' % name)


def sendTodaysMinutesDuty(message, args):
    name = repo.presentMinutes()
    message.send('本日の議事録当番は%sさんです。よろしくお願いします。' % name)


# @respond_to(r'^(?=.*[ごみ|ゴミ|trash|garbage])(?=.*[終|done])(?=2525).*$')
# def whosNext():


# @respond_to(r'^(?=.*[議事録])(?=.*[終|done]).*$')
# def whosNextMinutes():


@respond_to(r'^ping\s+\d+\.\d+\.\d+\.\d+\s*$')
def pingReply(message):
    message.reply('それはpingのコマンドですね。実行できませんが。')


count = 0


@default_reply()
def easterEgg(message, args):
    global count
    count += 1
    message.reply('received'+args)
    if count % 500 == 0 and count < 1000:
        message.reply('{}回目の意味のないメッセージを受信しました！この調子です！！！'.format(str(count)))
        message.react('+1')
    elif count % 100 == 0 and count < 1000:
        message.reply('{}回目の意味のないメッセージを受信しました！おめでとうございます！！！'.format(str(count)))
        message.react('+1')
    elif count == 1000:
        message.reply('{}回目の意味のないメッセージを受信しました！私の完敗です...！！！'.format(str(count)))
        message.reply('これ以上は何もありません！！！')
        message.react('+1')
