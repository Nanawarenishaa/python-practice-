'''def PrimeNo(num):
    for i in range(2,num):
        IsPrime=True
        for j in range(2,i):
            if i%j==0:
                IsPrime=False
                break
        if IsPrime:
            print(i,end=" ")
number= int(input("Enter num:"))
PrimeNo(number)'''

'''def reverseStr(str):
    words=str.split()
    reversed=[]

    for word in words:
        reversed.append(word[::-1])
    return " ".join(reversed)

string=input("Enter sentence/string:")
print(reverseStr(string))'''


'''rows=int(input("Enter rows:"))
cols=int(input("Enter cols:"))


A=[]
B=[]

print("Enter first matrix:")
for r in range(rows):
    row=[]
    for c in range(cols):
        row.append(int(input()))
    A.append(row)

print("Enter second matrix:")
for r in range(rows):
    row=[]
    for c in range(cols):
        
        row.append(int(input()))
    B.append(row)

print("Addition of two matrix:")
result=[]

for r in range(rows):
    row=[]
    for c in range(cols):
        row.append(A[r][c]+B[r][c])
    result.append(row)
print("Display:")
for i in result:
    print(i)'''

class InvalidInput:
    pass

def Factorial(num):
    if num < 0 :
        raise InvalidInput("invalid Input: enter positive number")

    fact=1
    for n in range(1,num+1):
        fact=fact*n
    print(f"factorial number of {num}:{fact}")

try:
    number=int(input("enter num:"))
    Factorial(number)
except InvalidInput as e:
    print(e)
except InvalidError:
    print("Invalid input:")

          
        
    
           


    
            

        








