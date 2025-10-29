max=int(input("enter value:"))
stack=[None]*max
top=-1


def isFull():
   return top == max-1

def isEmpty():
   return top == -1

def push():
   global top
   if isFull():
      print("stack overflow!")
   else:
      item = int(input("enter data to insert:"))
      top += 1
      stack[top]=item
      print(item," push successfully!")

def pop():
   global top
   if isEmpty():
      print("stack underflow!")
   else:
      item=stack[top]
      stack[top]=None
      top -= 1
      print(item,"remove successfully")

def peek():
   if isEmpty():
      print("stack is empty.")
   else:
      print("peek element from stack is :",stack[top])

def display():
   if isEmpty():
      print("stack is empty")
   else:
      print("current stack (top -> bottom):",stack[:top+1])

while True:
   print("1.push element \n2.pop element \n3.check peek element \n4.check isFull \n5.check isEmpty \n6.display stack \n7.Exit")
   ch = int(input("enter choice:"))  
   if ch==1:
      push()
   elif ch==2:
      pop()
   elif ch==3:   
      peek()
   elif ch==4:
     print("Is stack full?",isFull()) 
   elif ch==5:
     print("Is stack Empty?",isEmpty()) 
   elif ch==6:
      display()
   elif ch==7:
      print("program exiting...")
      break
   else:
      print("enter valid choice,please try again!")
    