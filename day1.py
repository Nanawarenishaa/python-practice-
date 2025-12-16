

student = {
    "name": "Nisha",
    "age": 20,
    "course": "Computer Science",
    "college": "ABC College",
    "city": "Pune"
}

print("Keys in the dictionary:")
for key in student.keys():
    print(key)
 
student["grade"] = "A"
print("\nAfter adding new key-value pair:")
print(student)

del student["city"]
print("\nAfter deleting a specific key:")
print(student)
 
student["age"] = 21
print("\nAfter modifying value of a key:")
print(student)
