names=["Ajay","Vijay","Ganesh","Paresh","Mahesh"]
firstLetter=[]
#firstLetter=[name[0] for name in names]
for name in names:
    firstLetter.append(name[0])
print("input names:", names)
print("output list",firstLetter)