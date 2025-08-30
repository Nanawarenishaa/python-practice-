""" num1 = int(input("Enter first number: "))
num2 = int(input("Enter first number: "))

def Addition( a , b):
    return a + b

result= Addition(num1,num2)
print(result) """

# number is even or odd

num = int(input("Enter value to check if even or odd: "))

if num % 2 == 0 :
    print(num," is a even number. ")
else:
    print(num," is a odd number.")

# check maximum number in three values

num1 = int(input("Enter first number: "))
num2 = int(input("Enter first number: "))
num3 = int(input("Enter first number: "))

if num1 >= num2 and num1 >= num3:
    print(num1," is a maximum number")
elif num2 >= num1 and num2 >= num3:
    print(num2," is a maximum number.")
else :
    print(num3," is a maximum number.")