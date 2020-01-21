from logs.LogHandler import LogHandler
from plugins.SQLRepository import SQLRepository

class Node:
    """
    In this class, Member class is substituet class for 'Node'
    """

    def __init__(self, data): 
        self.data = data  
        self.next = None


class Member:

    def __init__(self, slackid, name, grade, onDuty=False, cursor=False, willBeSkipped=False):
        self.slackid = slackid
        self.name = name
        self.grade = grade  #TODOができればいらない
        self.onDuty = onDuty
        self.cursor = cursor
        self.willBeSkipped = willBeSkipped
        self.next = None
    

class CircularLinkedList:
    

    def __init__(self, job=None):
        self.head = None

        repo = SQLRepository()
        if job == 'minutes':
            idList = repo.getMemberInfo4Minutes()
            for r in idList:
                if r[3]:
                    m = Member(slackid=r[0], name=r[1], grade=r[2], onDuty=bool(r[3]), cursor=True)
                else:
                    m = Member(slackid=r[0], name=r[1], grade=r[2], onDuty=bool(r[3]))
                self.push(m)
            self.printList()
        elif job == '2525':
            info = repo.getMemberInfo4Trash('2525')
            for i in info:
                if i[3]:
                    m = Member(slackid=i[0], name=i[1], grade=i[2], onDuty=bool(i[3]), cursor=True)
                else:
                    m = Member(slackid=i[0], name=i[1], grade=i[2], onDuty=bool(i[3]))
                self.push(m)
        elif job == '2721':
            info = repo.getMemberInfo4Trash('2721')
            for i in info:
                if i[3]:
                    m = Member(slackid=i[0], name=i[1], grade=i[2], onDuty=bool(i[3]), cursor=True)
                else:
                    m = Member(slackid=i[0], name=i[1], grade=i[2], onDuty=bool(i[3]))
                self.push(m)

    def push(self, data):
        if type(data) is Member:
            ptr1 = data
        else:
            ptr1 = Member(data)
        temp = self.head

        ptr1.next = self.head 
  
        # If linked list is not None then set the next of 
        # last node 
        if self.head is not None: 
            while(temp.next != self.head):
                temp = temp.next 
            temp.next = ptr1 
  
        else: 
            ptr1.next = ptr1 # For the first node 
  
        self.head = ptr1  
  
    # Extend this.
    def search(self, value):
        cur = self.head

        while cur != None:
            if cur.data == value:
                return True
            else:
                cur = cur.next

            if cur == self.head:
                return False
                break
    
    def searchMember(self, slackid):
        current = self.head
        try:
            while current != None:
                if current.slackid == slackid:
                    return current
                else:
                    current = current.next

                if current == self.head:
                    raise Exception('slack id not found.')
                    break
        except Exception as e:
            pass
            #logs.logException(e)

    def searchMinutes(self):
        current = self.head

        try:
            while current != None:
                if current.onDuty:
                    return current
                else:
                    current = current.next

                if current == self.head:
                    raise Exception('Nobady is on duty of minutes')
                    break
        except Exception as e:
            pass
            #logs.logException(e)

    def searchonCursor(self):
        current = self.head
        try:
            while current != None:
                if current.cursor:
                    return current
                else:
                    current = current.next

                if current == self.head:
                    raise Exception('Nobady has cursor in this list')
                    break
        except Exception as e:
            pass
            #logs.logException(e)

    def setCursorNext(self):
        current = self.searchonCursor()
        current.cursor = False
        current.next.cursor = True
    
    def willBeSkippedDuty(self, slackID):
        target = self.searchMember(slackID)

    def printList(self): 
        temp = self.head 
        if self.head is not None: 
            while(True): 
                print ('name:%s, onDuty:%s, cursor:%s, willBeSkipped:%s' % (temp.name, temp.onDuty, temp.cursor, temp.willBeSkipped))
                temp = temp.next
                if (temp == self.head): 
                    break
