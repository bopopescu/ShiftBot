# coding: utf-8
from logs import LogHandler as logs

import configparser
import sys

import mysql.connector as sql

parser = configparser.ConfigParser()
parser.read("./mysql.ini")

transaction = sql.connect(
    host=parser["sql"]["host"],
    port=parser["sql"]["port"],
    user=parser["sql"]["user"],
    password=parser["sql"]["password"],
    database=parser["sql"]["database"]
)

transaction.ping(reconnect=True)
cursor = transaction.cursor()


def mod(num, size):
    q, m = divmod(num, size)
    if m != 0:
        return m
    else:
        return size


def getSlackIDofMinutesDuty(*grade):
    pres = None
    try:
        cursor.execute("select SLID from members where behalf_minutes = TRUE")
        result = cursor.fetchone()
        pres = result[0]
    except TypeError as te:
        # 曜日ごとに発表学年が違う場合(卒論対応時期)
        if grade is not None:
            cursor.execute("select SLID from members where grade not in ('b3', '%s') and onDuty_minutes = TRUE" % grade)
        # 通常時(2人/1回)の場合
        else:
            cursor.execute("select SLID from members where onDuty_minutes = TRUE")
        result = cursor.fetchone()
        pres = result[0]
    except Exception as e:
        logs.logException(e)
    return pres


def getSlackIDofTrashDuty(room):
    pres = None
    try:
        cursor.execute("select SLID from members where room = '%s' and behalf_trash = TRUE" % room)
        result = cursor.fetchone()
        if result is not None:
            pres = result[0]
        else:
            cursor.execute("select SLID from members where room = '%s' and onDuty_trash = TRUE" % room)
            result = cursor.fetchone()
            pres = result[0]
    except Exception as e:
        logs.logException(e)
    return pres        


def getNamebySlackID(slackID):
    try:
        cursor.execute("select name from members where SLID = '%s'" % slackID)
        result = cursor.fetchone()
    except Exception as e:
        logs.logException(e)
    return result[0]


def presentTrash(room):
    """ 部屋番号を引数として受け取り,次回のゴミ捨て当番の名前を返す.

    部屋番号(str)を引数として受け取り,
    当該部屋の代理のごみ捨て当番(behalf_trashがTrue)が存在するか確認.
    存在した場合,その代理のごみ捨て当番の名前を返す.
    存在しなかった場合,順番通りのごみ捨て当番の名前を返す.

    Args:
        room    (str) : 4桁の部屋番号(2525or2721)

    Returns:
        pres    (str) : 次回のごみ捨て当番者の名前(名字)
    """    
    pres = None
    try:
        cursor.execute("select name from members where room = '%s' and behalf_trash = TRUE" % room)
        result = cursor.fetchone()
        pres = result[0]
    except TypeError as te:
        cursor.execute("select name from members where room = '%s' and onDuty_trash = TRUE" % room)
        result = cursor.fetchone()
        pres = result[0]
    except Exception as e:
        logs.logException(e)
    return pres


def nextTrashbyID(slackID):
    cursor.execute("select room from members where SLID = '%s'" % slackID)
    result = cursor.fetchone()
    room = result[0]
    doneTrashDutyBehalfOf(room)
    return (room, nextTrash(room))


def nextTrash(room):
    """ 部屋番号を引数として受け取りごみ捨て当番を更新した後,次回のゴミ捨て当番の名前を返す.

    部屋番号(str)を引数として受け取り,当該部屋のごみ捨て当番の順番を変数 order に代入.
    次に部屋番号から,当該部屋の総人数を変数 mem に代入.
    order と mem の内容から,次回のごみ捨て当番を決定し,データベースを更新する.
    更新後,presentTrash()メソッドを呼出すことで,次回のごみ捨て当番の名前を返す.

    Args:
        room    (str) : 4桁の部屋番号(2525or2721)

    Returns:
        presentTrash(room)    (str) : 次回のごみ捨て当番者の名前(名字)
    """

    cursor.execute("select trashDuty_order from members where room = '%s' and onDuty_trash = TRUE" % room)
    result = cursor.fetchone()
    order = int(result[0])

    cursor.execute("select count(*) from members where room = '%s' and trashDuty_order is not NULL group by room" % room)
    result = cursor.fetchone()
    mem = int(result[0])

    try:
        cursor.execute("update members set onDuty_trash = FALSE where room = '%s' and trashDuty_order = '%s'" % (room, order))
        cursor.execute("update members set onDuty_trash = TRUE where room = '%s' and trashDuty_order = '%s'" % (room, mod(order + 1, mem)))
    except Exception as e:
        transaction.rollback()
        logs.logException(e)
    else:
        transaction.commit()
    return presentTrash(room)


def prevTrash(room):
    """ 部屋番号を引数として受け取り,ごみ捨て当番を一つ前の状態に更新する.

    部屋番号(str)を引数として受け取り,当該部屋のごみ捨て当番の順番を変数 order に代入.
    次に部屋番号から,当該部屋の総人数を変数 mem に代入.
    order と mem の内容から前回のごみ捨て当番を決定し,データベースを更新する.
    間違えて更新してしまったときなど管理,テスト用.

    Args:
        room    (str) : 4桁の部屋番号(2525or2721)

    Returns:
        presentTrash(room)    (str) : 次回のごみ捨て当番者の名前(名字)
    """

    cursor.execute("select trashDuty_order from members where room = '%s' and onDuty_trash = TRUE" % room)
    result = cursor.fetchone()
    order = int(result[0])

    cursor.execute("select count(*) from members where minutesDuty_order is not null")
    rs = cursor.fetchone()
    mem = int(rs[0])

    try:
        cursor.execute("update members set onDuty_trash = FALSE where room = '%s' and trashDuty_order = '%s'" % (room, order))
        cursor.execute("update members set onDuty_trash = TRUE where room = '%s' and trashDuty_order = '%s'" % (room, mod(order - 1, mem)))
        transaction.commit()
    except Exception as e:
        transaction.rollback()
        logs.logException(e)


def presentMinutes(*grade):
    """ 次回の議事録当番の名前を返す.

    はじめに代理の議事録当番(behalf_minutesがTrue)が存在するか確認.
    存在した場合,その代理の議事録当番の名前を返す.
    存在しなかった場合,順番通りの議事録当番の名前を返す.

    Args:

    Returns:
        pres    (str) : 次回の議事録当番者の名前(名字)
    """

    pres = None
    try:
        cursor.execute("select name from members where behalf_minutes = TRUE")
        result = cursor.fetchone()
        pres = result[0]
    except TypeError as te:
        if grade is not None:
            cursor.execute("select name from members where grade not in ('b3', '%s') and onDuty_minutes = TRUE" % grade)
        else:
            cursor.execute("select name from members where onDuty_minutes = TRUE")
        result = cursor.fetchone()
        pres = result[0]
    except Exception as e:
        logs.logException(e)
    return pres


def nextMinutes():
    """ 議事録当番を更新した後,次回の議事録当番の名前を返す.

    はじめに議事録当番の順番を変数 order に代入.
    次に議事録当番を回しているメンバーの総数を変数 mem に代入
    order と mem の内容から次回の議事録当番を決定し,データベースを更新する.
    更新後,presentMinutes()メソッドを呼出すことで,更新後の議事録当番の名前を返す.

    Args:

    Returns:
        presentTrash(room)    (str) : 次回のごみ捨て当番者の名前(名字)
    """

    cursor.execute("select minutesDuty_order from members where onDuty_minutes = TRUE")
    result = cursor.fetchone()
    order = int(result[0])

    cursor.execute("select count(*) from members where minutesDuty_order is not null")
    rs = cursor.fetchone()
    mem = int(rs[0])
    try:
        cursor.execute("update members set onDuty_minutes = FALSE where minutesDuty_order = '%s'" % order)
        cursor.execute("update members set onDuty_minutes= TRUE where minutesDuty_order = '%s'" % mod(order + 1, mem))
        transaction.commit()
        return presentMinutes()
    except Exception as e:
        transaction.rollback()
        logs.logException(e)


def nextMinutesInBusySeason(prevGrade):
    cursor.execute("select kanaOrder_grade from members where grade = '%s' and onDuty_minutes = TRUE" % prevGrade)
    result = cursor.fetchone()
    order = int(result[0])

    cursor.execute("select count(*) from members where grade = '%s' and kanaOrder_grade is not null" % prevGrade)
    rslt = cursor.fetchone()
    mem = int(rslt[0])

    try:
        cursor.execute("update members set onDuty_minutes = FALSE where kanaOrder_grade = '%s'" % order)
        cursor.execute("update members set onDuty_minutes= TRUE where kanaOrder_grade = '%s'" % mod(order + 1, mem))
        transaction.commit()
        return presentMinutes(prevGrade)
    except Exception as e:
        transaction.rollback()
        logs.logException(e)


def trashDutyBehalfOf(slackID):
    """
    動作確認：未
    """

    try:
        cursor.execute("update members set behalf_trash = TRUE where SLID = '%s'" % slackID)
    except Exception as e:
        transaction.rollback()
        logs.logException(e)
    else:
        transaction.commit()
    return getNamebySlackID(slackID)


def minutesDutyBehalfOf(slkid):
    """ 代理の議事録当番を登録する.

    引数として受け取ったuserIDから代理の議事録当番を決定し,データベースを更新する.
    更新後,presentMinutes()を呼び出し,議事録当番の名前を返す.

    Args:
        slkid   (str) : 代理で議事録当番をする人(送信者)のSlackID

    Returns:
        presentMinutes()    (str) : 次回の議事録当番者の名前(名字)

    """
    try:
        cursor.execute("update members set behalf_minutes = TRUE where SLID = '%s'" % slkid)
    except Exception as e:
        transaction.rollback()
        logs.logException(e)
    else:
        transaction.commit()
    return presentMinutes()


def doneTrashDutyBehalfOf(room):
    """
    動作確認：未
    """

    try:
        cursor.execute("select name from members where room = '%s' and behalf_trash = TRUE" % room)
        result = cursor.fetchone()
        name = result[0]
        cursor.execute("update members set behalf_trash = FALSE where name = '%s'" % name)
    except Exception as e:
        transaction.rollback()
        logs.logException(e)
    else:
        transaction.commit()


def doneMinutesDutyBehalfOf():
    """
    代理の議事録当番を解除する.

    Returns:
        None
    """
    try:
        cursor.execute("select name from members where behalf_minutes = TRUE")
        result = cursor.fetchone()
        name = result[0]
        cursor.execute("update members set behalf_minutes = FALSE where name = '%s'" % name)
    except TabError as te:
        return
    except Exception as e:
        transaction.rollback()
        logs.logException(e)
    else:
        transaction.commit()

