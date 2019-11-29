# coding: utf-8
import configparser
import sys

import mysql.connector as sql

parser = configparser.ConfigParser()
parser.read('./mysql.ini')

transaction = sql.connect(
    host=parser['sql']['host'],
    port=parser['sql']['port'],
    user=parser['sql']['user'],
    password=parser['sql']['password'],
    database=parser['sql']['database']
)

cursor = transaction.cursor()


def mod(num, size):
    q, m = divmod(num, size)
    if m != 0:
        return m
    else:
        return size


def ping(self):
    # 定期的に実行
    self.cursor.ping(reconnect=True)


def presentTrash(room):
    try:
        cursor.execute('select name from members where room = %s and behalf_trash = TRUE' % room)
        result = cursor.fetchall()
        pres = result[0]
    except Exception as e:
        cursor.execute('select name from members where room = %s and onDuty_trash = TRUE' % room)
        result = cursor.fetchone()
        print(result)
        pres = result[0]
    return pres


def nextTrash(room):
    cursor.execute('select trashDuty_order from members where room = %s and onDuty_trash = TRUE' % room)
    result = cursor.fetchone()
    order = int(result[0])

    if room == '2525':
        mem = 8
    elif room == '2721':
        mem = 5
    try:
        cursor.execute('update members set onDuty_trash = FALSE where room = %s and trashDuty_order = %s' % (room, order))
        transaction.commit()
        cursor.execute('update members set onDuty_trash = TRUE where room = %s and trashDuty_order = %s' % (room, mod(order + 1, mem)))
        transaction.commit()
    except Exception as e:
        transaction.rollback()
        tb = sys.exc_info()[2]
        e.with_traceback(tb)
        raise
    return presentTrash(room)


def prevTrash(room):
    cursor.execute('select trashDuty_order from members where room = %s and onDuty_trash = TRUE' % room)
    result = cursor.fetchone()
    order = int(result[0])

    if room == '2525':
        mem = 8
    elif room == '2721':
        mem = 5
    try:
        cursor.execute('update members set onDuty_trash = FALSE where room = %s and trashDuty_order = %s' % (room, order))
        cursor.execute('update members set onDuty_trash = TRUE where room = %s and trashDuty_order = %s' % (room, mod(order - 1, mem)))
        transaction.commit()
    except Exception as e:
        transaction.rollback()
        tb = sys.exc_info()[2]
        e.with_traceback(tb)
        raise


def presentMinutes():
    try:
        cursor.execute('select name from members where behalf_minutes = TRUE')
        result = cursor.fetchone()
        pres = result[0]
    except Exception as e:
        print(e)
        cursor.execute('select name from members where onDuty_minutes = TRUE')
        result = cursor.fetchone()
        pres = result[0]
    return pres


def nextMinutes():
    cursor.execute('select minutesDuty_order from members where onDuty_minutes = TRUE')
    result = cursor.fetchone()
    order = int(result[0])
    try:
        cursor.execute('update members set onDuty_minutes = FALSE where minutesDuty_order = %s' % order)
        cursor.execute('update members set onDuty_minutes= TRUE where minutesDuty_order = %s' % mod(order + 1))
        transaction.commit()
        return presentMinutes()
    except Exception as e:
        transaction.rollback
        tb = sys.exc_info()[2]
        e.with_traceback(tb)
        raise


def behalfOfTrash(room, name):
    duty = presentTrash(room)
    cursor.execute('update members set behalf_trash = TRUE where name = %s' % name)
    transaction.commit()
    return duty


def behalfOfMinutes(name):
    duty = presentTrash()
    cursor.execute('update members set behalf_minutes = TRUE where name = %s' % name)
    transaction.commit()
    return duty


def doneBehalfOfTrash():
    try:
        cursor.excute('select name from members where behalf_trash = TRUE')
        result = cursor.fetchone()
        name = result[0]
        cursor.execute('update members set behalf_trash = FALSE where name = %s' % name)
        transaction.commit()
    except Exception as e:
        tb = sys.exc_info()[2]
        e.with_traceback(tb)


def doneBehalfOfMinutes():
    try:
        cursor.excute('select name from members where behalf_minutes = TRUE')
        result = cursor.fetchone()
        name = result[0]
        cursor.execute('update members set behalf_minutes = FALSE where name = %s' % name)
        transaction.commit()
    except Exception as e:
        tb = sys.exc_info()[2]
        e.with_traceback(tb)
