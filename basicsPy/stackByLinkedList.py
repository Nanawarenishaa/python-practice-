class Node:
    def __init__(self,data):
        self.data=data
        self.next=None

class stackByLinkedList:
    def __init__(self):
        self.top=None
    
    def push(self,data):
        newNode=Node(data)      
        newNode.next=self.top
        self.top=newNode 
        print(f"{data} inserted successfully!")
    def display(self):
        temp=self.top
        while temp:
            print(temp.data,end="->")
            temp=temp.next
        print("None")
    def pop(self):
        ele=self.top.data
        print(f"{ele} remove successfully")

SBLL=stackByLinkedList()
while True:
    print("1.push element \n2.display elements \n3.Exit")
    ch=int(input("Enter your choice:"))
    if ch == 1:
       data=int(input("enter data:"))
       SBLL.push(data) 
    elif ch==2:
       SBLL.display()
    elif ch==3:
        print("existing program...")
        break
    else:
        print("enter valid choice!please try again..")