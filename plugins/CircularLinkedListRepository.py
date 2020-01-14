from plugins.CircularLinkedList import CircularLinkedList

class CircularLinkedListRepository:

    def __init__(self):
        self.minutes = CircularLinkedList('minutes')
        self.trash2525 = CircularLinkedList()
        self.trash2721 = CircularLinkedList()
    
    def presantTrash(self, room=None):
        m2525 = self.trash2525.searchTrash()
        m2721 = self.trash2721.searchTrash()
        if room == '2525':
            return m2525.name
        elif room == '2721':
            return m2721.name
        else:
            return (m2525.name, m2721.name)
    
    def nextTrashin2525(self):
        prev = self.trash2525.searchonCursor()
        prev.isTrash = False
        prev.next.isTrash = True
        return prev.next.name

    def nextTrashin2721(self):
        prev = self.trash2721.searchonCursor()
        prev.isTrash = False
        prev.next.isTrash = True
        return prev.next.name

    def presantMinutes(self):
        member = self.minutes.searchMinutes()
        return member.name

    def nextMinutes(self, nextSpeaker):
        print('befor:')
        self.minutes.printList()
        prev = self.minutes.searchMinutes()
        if prev.cursor == False:
            prev.willBeSkipped = True

        cur = self.minutes.searchonCursor()

        while cur.next != None:
            print('調べる対象：'+cur.name)
            # 確認対象の人が変更前の議事録当番であれば
            # カーソルを次の人に移し次の人を確認
            if cur.isMinutes:
                print('確認対象の人が変更前の議事録当番であればカーソルを次の人に移し次の人を確認')
                cur.cursor = False
                cur.next.cursor = True
                cur = cur.next
            # 確認対象の人が変更前の議事録当番でなければ，
            else:
                print('確認対象の人が変更前の議事録当番でなければ，')
                # skipフラグがTrueならフラグをFalseにし，
                # カーソルを次の人に移し，次の人を確認
                if cur.willBeSkipped:
                    print('skipフラグがTrueならフラグをFalseにし，カーソルを次の人に移し，次の人を確認')
                    if cur.cursor:
                        cur.willBeSkipped = False
                        cur.cursor = False
                        cur.next.cursor = True
                    cur = cur.next
                # skipフラグFalseで次回の発表者ならカーソルを保持したまま次の人を確認
                elif cur.grade == nextSpeaker:
                    print('skipフラグFalseで次回の発表者ならカーソルを保持したまま次の人を確認')
                    cur = cur.next
                # skipフラグFalseかつ次回の発表者でなければその人を次の議事録当番に設定
                else:
                    print('skipフラグFalseかつ次回の発表者でなければその人を次の議事録当番に設定')
                    cur.isMinutes = True
                    prev.isMinutes = False
                    break
        print('after:')
        self.minutes.printList()

        return cur.name
        
