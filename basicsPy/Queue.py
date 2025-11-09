queue=[]

def enqueue():
    element=int(input("enter element:"))
    queue.append(element)
    print(f"{element} is added successfully!")

def dequeue():
    if not queue:
        print("Queue is empty! cannot dequeue element.")
    else:
        element=queue.pop()
        print(f"{element} removed..")

def display():
    if not queue:
        print("queue is empty")
    else:
        print("Current queue:",queue)

while True:
    print("1.Enqueue \n2.Dequeue \n3.Display \n4.Exit.")
    ch = int(input("Enter your choice:"))
    if ch == 1:
        enqueue()
    elif ch == 2:
        dequeue()
    elif ch == 3:
        display()
    elif ch == 4:
        print("program exiting...")
        break 
    else:
        print("Invalid choice! please try again...")