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
            
    def insert_at_position(self,data,pos):
        newNode=Node(data)
        if pos == 1:
            newNode.next=self.head
            self.head=newnode
            return
        temp=self.head
        count=1
        while temp and count < pos-1:
            temp=temp.next
            count+=1
        if temp is None:
            print("pos out os range")
        
        newNode.next=temp.next
        temp.next=newNode
        

    def display(self):
        if self.head is None:
            print("linked is empty!")
        else:
            temp=self.head
            while temp:
                print(temp.data,end="->")
                temp=temp.next
            print("None")

    
    def reverse(self):
          prev=None
          temp=self.head
          while temp:
              nxt=temp.next
              temp.next=prev
              prev=temp
              temp=nxt
          self.head=prev
        
    def sorted(self):
        
         if self.head is None:
            print("linked is empty!")
            return
         values=[]
         
         temp=self.head
         while temp:
                values.append(temp.data)
                temp=temp.next
         values.sort()
         print("sorted list:",values)
ll=LinkedList()

while True:
    print("1.insert_end")
    print("2.Display")
    print("3.Sort")
    print("4.inser_at_end")
    print("5.reverse")
    print("5.Exit")

    ch= int(input("Enter choice:"))
    
    if ch == 1:
            d=int(input("Enter data:"))
            ll.insert_end(d)
    elif ch == 2:

            ll.display()
    elif ch == 3:
            ll.sorted()
    elif ch == 4:
            d = int(input("Enter data: "))
            p = int(input("Enter position: "))
            ll.insert_at_position(d, p)
    elif ch == 5:
            ll.reverse()      
    elif ch == 6:
            print("program exiting...")
            break
    else:
            print("enter valid choice!!")
                

