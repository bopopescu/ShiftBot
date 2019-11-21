import configparser

import mysql

sql_conf = configparser.ConfigParser().read('./mysql.ini')

transaction = mysql.connector.connect(
    host=sql_conf['sql']['host'],
    port=sql_conf['sql']['port'],
    user=sql_conf['sql']['user'],
    password=sql_conf['sql']['password'],
    database=sql_conf['sql']['database']
)

cur = transaction.cursol()


def mod(num, size):
    q, m = divmod(size, num)
    if m != 0:
        return m
    else:
        return size


def ping(self):
    # 定期的に実行
    self.ysql.ping(reconnect=True)


def presentTrash(self, room):
    try:
        pres = cur.excute('select name from members where room = %s and behalf_trash = TRUE', [room])
    except Exception as e:
        print(e)
        pres = cur.excute('select name from members where room = %s and onDuty_trash = TRUE', [room])
    return pres


def nextTrash(self, room):
    order = cur.excute('select trashDuty_order from members where room = %s and onDuty_trash = True', [room])
    if room == '2525':
        mem = 10
    elif room == '2721':
        mem = 5
    try:
        cur.excute('update members set onDuty_trash = FALSE where room = %s and trashDuty_order = %s', [room, order])
        cur.excute('update members set onDuty_trash = TRUE where room = %s and trashDuty_order = %s', [room, mod(order+1, mem)])
        transaction.commit()
        return presentTrash(room)
    except Exception as e:
        transaction.rollback()
        print(e)
        raise


def prevTrash(self, room):
    order = cur.excute('select trashDuty_order from members where room = %s and onDuty_trash = True', [room])
    if room == '2525':
        mem = 10
    elif room == '2721':
        mem = 5
    try:
        cur.excute('update members set onDuty_trash = FALSE where room = %s and trashDuty_order = %s', [room, order])
        cur.excute('update members set onDuty_trash = TRUE where room = %s and trashDuty_order = %s', [room, mod(order-1, mem)])
        transaction.commit()
    except Exception as e:
        transaction.rollback()
        print(e)
        raise


def presentMinutes():
    try:
        pres = cur.excute('select name from members where behalf_minutes = TRUE')
    except Exception as e:
        print(e)
        pres = cur.excute('select name from members where onDuty_minutes = TRUE')
    return pres


def nextMinutes():
    order = cur.excute('select minutesDuty_order from members where onDuty_minutes = true')
    try:
        cur.excute('update members set onDuty_minutes = false where minutesDuty_order = %s', order)
        cur.excute('update members set onDuty_minutes= TRUE where minutesDuty_order = %s', mod(order+1))
        transaction.commit()
        return presentMinutes()
    except Exception as e:
        transaction.rollback
        raise


def behalfOfTrash(self, room, name):
    duty = presentTrash(room)
    cur.excute('update members set behalf_trash = TRUE where name = %s', name)
    transaction.commit()
    return duty


def behalfOfMinutes(self, name):
    duty = presentTrash()
    cur.excute('update members set behalf_minutes = TRUE where name = %s', name)
    transaction.commit()
    return duty


def doneBehalfOfTrash():
    try:
        name = cur.excute('select name from members where behalf_trash = true')
        cur.excute('update members set behalf_trash = false where name = %s', name)
        transaction.commit()
    except Exception as e:
        return print(e)


def doneBehalfOfMinutes():
    try:
        name = cur.excute('select name from members where behalf_minutes = true')
        cur.excute('update members set behalf_minutes = false where name = %s', name)
        transaction.commit()
    except Exception as e:
        return print(e)
