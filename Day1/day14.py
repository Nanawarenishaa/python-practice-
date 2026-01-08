class Node:
    def __init__(self,data):
        self.data=data
        self.next=None
class LinkedList:
    def __init__(self):
        self.head=None
    def insert_end(self,data):
        newNode=Node(data)
        if self.head is None:
            self.head=newNode
        else:
            temp=self.head
            while temp.next:
                temp=temp.next
            temp.next=newNode

    def display(self):
        if self.head is None:
            print("List is empty!")
        else:
            temp=self.head
            while temp:
                print(temp.data,end=" ")
                temp=temp.next
            print("None")
ll=LinkedList()

while True:
    print("1.insert_end")
    print("2.Display")
    print("3.Exit")

    ch= int(input("Enter choice:"))
    
    if ch == 1:
            d=int(input("Enter data:"))
            ll.insert_end(d)
    elif ch == 2:
            ll.display()
    elif ch == 3:
            print("program exiting...")
            break
    else:
            print("enter valid choice!!")
            
    

            
