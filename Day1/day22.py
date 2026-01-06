num=int(input("enter of element:"))
str=set()

for i in range(num):
    j=input("enter character:")
    str.add(j)

print("Elements:",str)
print("length of set:",len(str))

digits=0
lowerCase=0
upperCase=0

for ch in str:
    if ch.isdigit():
        digits+=1
    elif ch.islower():
        lowerCase+=1
    elif ch.isupper():
        upperCase+=1

print("digits:",digits)
print("lowercase:",lowerCase)
print("uppercase:",upperCase)
