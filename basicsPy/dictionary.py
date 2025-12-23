
'''Student={
    "name":"Nisha",    "rollNo":83,
    "Age":21,
    "Course":"MCA",
    "Addr":"Karjat"
    }

print("Display Student Info:")
print(Student)

print("All keys in Dictionary:")
print(Student.keys())

print("dictionary after adding value:")
Student["Grade"]="B"
print(Student)

print("dictionary after updation:")
Student["Addr"]="Pune"
print(Student)

print(Student.values())

print("dictionary after deleting kay:")
del Student["rollNo"]
print(Student)'''

def reversedWords(Str):
    Words=Str.split()
    reverseArray=[]

    for i in Words:
        reverseArray.append(i[::-1])
    return " ".join(reverseArray)

string=input("Enter String:")
print(reversedWords(string))



