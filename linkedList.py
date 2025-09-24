class Node:
    def __init__(self,data):
        self.data=data
        self.next=None
    
class linkedList:
    def __init__(self):
        self.head=None

    def insertEnd(self,data):
        temp=Node(data)
        if self.head is None:
            self.head=temp
        else:
            newNode=self.data 
            while newNode.next:
                newNode=temp.next
            newNode.next=temp

    
            