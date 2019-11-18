import configparser

import mysql

sql_conf = configparser.ConfigParser().read('./mysql.ini')

ysql = mysql.connector.connect(
    host=sql_conf['sql']['host'],
    port=sql_conf['sql']['port'],
    user=sql_conf['sql']['user'],
    password=sql_conf['sql']['password'],
    database=sql_conf['sql']['database']
)

cur = ysql.cursol()


def mod(num, size):
    q, m = divmod(size, num)
    if m != 0:
        return m
    else:
        return size


def ping(self):
    # 定期的に実行
    self.ysql.ping(reconnect=True)


def nextTrash(self, room):
    order = cur.excute('select trashDuty_order from members where room = %s and onDuty_trash = True', [room])
    if room == '2525':
        mem = 10
    elif room == '2721':
        mem = 5
    try:
        cur.excute('update members set onDuty_trash = FALSE where room = %s and trashDuty_order = %s', [room, order])
        cur.excute('update members set onDuty_trash = TRUE where room = %s and trashDuty_order = %s', [room, mod(order+1, mem)])
        ysql.commit()
    except:
        ysql.rollback()
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
        ysql.commit()
    except:
        ysql.rollback()
        raise


def presentTrash(self, room):
    pres = cur.excute('select name from members where room = %s and onDuty_trash = TRUE', [room])
    return pres


# def reset(self):


def nextMinutes():
    order = cur.excute('select minutesDuty_order from members where onDuty_minutes = true')
    try:
        cur.excute('update members set onDuty_minutes = false where minutesDuty_order = %s', order)
        cur.excute('update members set onDuty_minutes= TRUE where minutesDuty_order = %s', mod(order+1))
        ysql.commit()
    except:
        ysql.rollback
        raise


def presentMinutes():
    pres = cur.excute('select name from members where onDuty_minutes = TRUE')
    return pres

