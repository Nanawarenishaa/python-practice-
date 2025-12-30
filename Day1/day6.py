


class InvalidInput(Exception):
    pass

def factorial(num):
    if num < 0:
        raise InvalidInput("Invalid Input:Enter Positive Number!!")

    fact = 1
    for n in range(1,num+1):
        fact=fact*n
    print(f"Factorial of {num} is :{fact}")

try:
    number=int(input("Enter number:"))
    factorial(number)
except InvalidInput as e:
    print(e)
except ValueError:
    print("InputError:Enter integer number!!")
