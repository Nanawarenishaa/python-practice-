student={
    "name":"Nisha",
    "course":"MCA",
    "Marks":87,
    "age":21
}

print(student.keys())
print(student.values())
student["addr"]="Pune"
print(student)

del student["Marks"]
print(student)

student["age"]=22
print(student)