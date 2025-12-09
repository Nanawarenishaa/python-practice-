import threading
import time
lock = threading.Lock()

def Odd(num):
    with lock:
        print("Odd numbers:")
        for i in range(num):
          if i%2!=0:
            print(i)
            time.sleep(0.5)

def Even(num):
   with lock:
      print("Even numbers:")
      for i in range(num):
         if i%2==0:
            print(i)
            time.sleep(0.5)

t1=threading.Thread(target=Odd,args=(10,))
t2=threading.Thread(target=Even,args=(10,))
t1.start()
t2.start()
t1.join()
t2.join()