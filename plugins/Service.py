# coding: utf-8
from slackbot.bot import respond_to

from plugins import Repository as repo


# 引数の数でエラー,むりやり
@respond_to(r'^(?=.*(ごみ|ゴミ))(?!.*(2525|2721|終)).*$')
def sendTrashDuty2525AND2721(message, args, room):

    """
    (ごみorゴミ)を含み,(2525or2721及び「終」)を含まないメッセージに対し
    両室の次回のごみ捨て当番をリプライする.


    Args:
        message (str) : メッセージを送信するための引数
        args    (str) : respond_to()内の正規表現にマッチしたメッセージ本文
        room    (str) : 4桁の部屋番号(2525or2721)

    Returns:
        None

    """

    name2525 = repo.presentTrash('2525')
    name2721 = repo.presentTrash('2721')
    message.send('次回のごみ捨て当番は\n2525室：%sさん\n2721室：%sさん\nです。' % (name2525, name2721))


@respond_to(r'^(?=.*(ごみ|ゴミ|trash|garbage))(?=.*2525)')
def sendTrashDutyIn2525(message, args):
    """
    (ごみorゴミ)を含み、かつ部屋番号「2525」が含まれているメッセージに対し
    2525室の次回のごみ捨て当番をリプライする。

    Args:
        message (str) : メッセージを送信するための引数
        args    (str) : respond_to()内の正規表現にマッチしたメッセージ本文

    Return:
        None
    """
    name = repo.presentTrash('2525')
    message.send('2525室の次回のごみ捨て当番は%sさんです。' % name)


@respond_to(r'^(?=.*(ごみ|ゴミ|trash|garbage))(?=.*2721)')
def sendTrashDutyIn2721(message, args):
    """
    (ごみorゴミ)を含み,かつ部屋番号「2721」が含まれているメッセージに対し
    2721室の次回のごみ捨て当番をリプライする.

    Args:
        message (str) : メッセージを送信するための引数
        args    (str) : respond_to()内の正規表現にマッチしたメッセージ本文

    Return:
        None
    """
    name = repo.presentTrash('2721')
    message.send('2721室の次回のごみ捨て当番は%sさんです。' % name)


@respond_to(r'(議事録|議事)')
def sendMinutesTaker(message, args):
    """
    (議事録or議事)が含まれているメッセージに対し
    次回の議事録当番をリプライする.

    Args:
        message (str) : メッセージを送信するための引数
        args    (str) : respond_to()内の正規表現にマッチしたメッセージ本文

    Return:
        None
    """
    message.reply(type(message))
    name = repo.presentMinutes()
    message.send('次回の議事録当番は%sさんです。' % name)


@respond_to(r'^(?=.*(ごみ|ゴミ))(?=.*終)')
def sendNextTrashDuty(message, args):
    """
    (ごみorゴミ)が含まれ,かつ「終」が含まれているメッセージに対し
    次回のゴミ捨て当番を更新し,その内容をリプライする.
    二部屋同時に更新されるので,両部屋のごみ捨てが終わったことを確認した後に実行する.

    Args:
        message (str) : メッセージを送信するための引数
        args    (str) : respond_to()内の正規表現にマッチしたメッセージ本文

    Return:
        None
    """
    name2525 = repo.nextTrash('2525')
    name2721 = repo.nextTrash('2721')
    message.send('''ありがとうございます。次回のごみ捨て当番は\n2525室：%sさん\n2721室：%sさん\nです。よろしくお願いします。''' % (name2525, name2721))


@respond_to(r'^(?=.*(議事録|議事))(?=.*終)')
def sendNextMinutesDuty(message, args):
    """
    (議事録or議事)が含まれ,かつ「終」が含まれているメッセージに対し
    次回の議事録当番を更新し,その内容をリプライする。
    定例ミーティング終了時に呼び出されることを想定している.

    Args:
        message (str) : メッセージを送信するための引数
        args    (str) : respond_to()内の正規表現にマッチしたメッセージ本文

    Return:
        None
    """
    name = repo.nextMinutes()
    message.send('''定例ミーティングお疲れさまです。\n
                    次回の議事録当番は%sさんです。よろしくお願いします。''' % name)


@respond_to(r'^(?=.*今日)(?=(議事録|議事))')
def sendTodaysMinutesDuty(message, args):
    """
    「今日」が含まれ,かつ(議事録or議事)が含まれているメッセージに対し
    次回の議事録当番をリプライする。
    メッセージの内容が変わっているのみで,sendMinutesTaker()と同じ動作をする.

    Args:
        message (str) : メッセージを送信するための引数
        args    (str) : respond_to()内の正規表現にマッチしたメッセージ本文

    Return:
        None
    """
    name = repo.presentMinutes()
    message.send('本日の議事録当番は%sさんです。よろしくお願いします。' % name)
