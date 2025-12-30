num=int(input("Enter number of elements:"))
s=set()

for i in range(num):
    i=input("Enter element:")
    s.add(i)


print("set elements:",s)
print("length of set:",len(s))

digits=0
uppercase=0
lowercase=0
for ch in s:
    if ch.isdigit():
        digits += 1

    elif ch.islower():
        lowercase+=1

    elif ch.isupper():
        uppercase+=1


print("Digits:",digits)
print("Lowercase:",lowercase)
print("uppercase:",uppercase)