from slackbot.slackclient import SlackClient as sc

from plugins import Repository as repo


def sendReminder4TrashDuty(client):
    text = '明日のごみ捨て当番です. よろしくお願いします. '
    id2525 = repo.getSlackIDofTrashDuty('2525')
    id2721 = repo.getSlackIDofTrashDuty('2721')
    sc.send_message(self=client, channel=id2525, message=text)
    sc.send_message(self=client, channel=id2721, message=text)


def sendReminder4FinishTrashDuty(client):
    text = "ごみ捨ては終わりましたか? 完了していれば「部屋番号(半角)+ごみ+終」を含む文を送信してください."
    id2525 = repo.getSlackIDofTrashDuty('2525')
    id2721 = repo.getSlackIDofTrashDuty('2721')
    sc.send_message(self=client, channel=id2525, message=text)
    sc.send_message(self=client, channel=id2721, message=text)


def sendReminder4MinutesDuty(client, *grade):
    text = '本日の議事録当番です. よろしくお願いします. '
    userid = repo.getSlackIDofMinutesDuty(grade)
    sc.send_message(self=client, channel=userid, message=text)