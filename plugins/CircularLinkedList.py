from plugins import Repository as repo

class Node:

    def __init__(self, data): 
        self.data = data  
        self.next = None


class Member:

    def __init__(self, slackid, isMinutes, isTrash):
        self.slackid = slackid
        self.isMinutes = isMinutes
        self.isTrash = isTrash


class CircularLinkedList:

    def __init__(self, job=None): 
        if job == 'minutes'
            idList = repo.getSlackIDList4MinutesOrder()
            for r in idList:
                minutes.push(r[0])
        else:
            self.head = None
  
    def push(self, data): 
        ptr1 = Node(data) 
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

    # Function to print nodes in a given circular linked list 
    def printList(self): 
        temp = self.head 
        if self.head is not None: 
            while(True): 
                print "%d" %(temp.data), 
                temp = temp.next
                if (temp == self.head): 
                    break
