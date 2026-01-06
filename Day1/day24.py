def my_range(start,stop,step):
    if step == 0 :
        raise ValueError("step cannot be zero!!")
    
    if step > 0:
        while start < stop:
            yield start
            start += step
    
    else:
        while start > stop:
            yield start
            start += step
start=int(input("Enter start value:"))
stop=int(input("Enter stop value:"))
step=int(input("Enter step value:"))

for value in my_range(start, stop, step):
    print(value,end=" ")
