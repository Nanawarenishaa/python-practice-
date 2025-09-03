
fruits = ["apple" , "banana" , "cherry"]

for i in fruits:
    print(i)

for num in range(1,5,1):
    print(num)

for i in range(5):
    for j in range(5):
      print("*", end=" ")
    print(end="\n")

rows=int(input("Enter raws you want to print:"))
for i in range(1,rows+1):
    print("*"*i)

rows = int(input("Enter rows you want to print: "))

for i in range(1, rows + 1):
    # print spaces first
    print(" " * (rows - i), end="")  
    
    # then print stars
    print("*" * (2 * i - 1))
