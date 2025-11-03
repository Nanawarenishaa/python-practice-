class Node:
    def __init__(self,data):
        self.data=data
        self.next=None
    
class LinkList:
    def __init__(self):
        self.head=None

    def insertData(self,data):
        newNode=Node(data)
        if self.head is None:
            self.head=newNode
            print(f"{data} inserted successfully!")
        else:
            temp=self.head
            while temp.next:
                temp=temp.next
            temp.next=newNode
            print(f"{data} inserted successfully!")

    def deleteLast(self):
         if self.head is None:
             print("List is empty Nothing to delete..")
             return
         if self.head.next is None:
             print(f"deleting last element:{self.head.data}")
             self.head=None
             return
         
         temp=self.head
         while temp.next.next:
             temp=temp.next
         print(f"deleting last element:{temp.next.data}")
         temp.next=None
    
    def deleteList(self):
        print("List deleted!")
        self.head=None



    def display(self):
        if self.head is Node:
            print("list is empty!")
        else:
            temp=self.head
            while temp:
                print(temp.data,end="->")
                temp=temp.next
            print("None")

LL=LinkList()



while True:
    print("1.insert data \n2.display \n3.delete last element \n4.delete List \n5.exit")
    ch=int(input("enter your choice:"))
    if ch==1:
       data=int(input("enter data:"))
       LL.insertData(data)
    elif ch==2:
        LL.display()
    elif ch==3:
        LL.deleteLast()
    elif ch==4:
        LL.deleteList()
    elif ch==5:
        print("existing program....")
        break
    else:
        print("invalid choice!please try again..")
         