from logs import LogHandler as logs
from plugins import Repository as repo

class Node:
    """
    In this class, Member class is substituet class for 'Node'
    """

    def __init__(self, data): 
        self.data = data  
        self.next = None


class Member:

    def __init__(self, slackid, name, grade, isTrash=False, isMinutes=False, cursor=False, willBeSkipped=False):
        self.slackid = slackid
        self.name = name
        self.grade = grade
        self.isTrash = isTrash
        self.isMinutes = isMinutes
        self.cursor = cursor
        self.willBeSkipped = willBeSkipped
        self.next = None
    

class CircularLinkedList:

    def __init__(self, job=None):
        self.head = None

        if job == 'minutes':
            idList = repo.getMemberInfo4Minutes()
            for r in idList:
                if r[4]:
                    m = Member(slackid=r[0], name=r[1], grade=r[2], isTrash=bool(r[3]), isMinutes=bool(r[4]), cursor=True)
                else:
                    m = Member(slackid=r[0], name=r[1], grade=r[2], isTrash=bool(r[3]), isMinutes=bool(r[4]))
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
            logs.logException(e)

    def searchMinutes(self):
        current = self.head

        try:
            while current != None:
                if current.isMinutes:
                    return current
                else:
                    current = current.next

                if current == self.head:
                    raise Exception('Nobady is on duty of minutes')
                    break
        except Exception as e:
            logs.logException(e)

    def searchTrash(self):
        current = self.head
        try:
            while current != None:
                if current.isTrash:
                    return current
                else:
                    current = current.next

                if current == self.head:
                    raise Exception('Nobady is on duty of trash')
                    break
        except Exception as e:
            logs.logException(e)

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
            logs.logException(e)

    def setCursorNext(self):
        current = self.searchonCursor()
        current.cursor = False
        current.next.cursor = True

    def printList(self): 
        temp = self.head 
        if self.head is not None: 
            while(True): 
                print ('name:%s, isMinutes:%s, cursor:%s, willBeSkipped:%s' % (temp.name, temp.isMinutes, temp.cursor, temp.willBeSkipped))
                temp = temp.next
                if (temp == self.head): 
                    break
