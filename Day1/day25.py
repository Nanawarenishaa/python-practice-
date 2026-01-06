class InvalidInput(Exception):
    pass

def factorial(num):
    if num < 0:
        raise InvalidInput("Invalid Input:enter positive number!!")
    
    else:
        fact=1
        for i in range(1,num-1):
            fact=fact*num
        print(f"factorial number of {num} is: ",fact)

try:
    number=int(input("enter input value:"))
    factorial(number)
except InvalidInput as e:
   print(e)

except ValueError:
    print("please enter integer value!!")




