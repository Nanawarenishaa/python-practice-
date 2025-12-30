import threading

def square(n):
    print("calculating squre...")
    print("square of number:",n*n)

def cube(n):
    print("calculating cube...")
    print("square of cube:",n*n*n)

num=int(input("Enter number:"))

t1=threading.Thread(target=square,args=(num,))
t2=threading.Thread(target=cube,args=(num,))

t1.start()
t1.join()
t2.start()
    
