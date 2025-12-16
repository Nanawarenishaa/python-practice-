from pymongo import MongoClient

client = MongoClient("mongodb://localhost:27017/")
db = client["College"]
students = db["students"]

student = {
    "Name": "Nisha",
    "Course": "MCA",
    "Age": 21
}

students.delete_many({"Name": "Nisha"})
print("Duplicate records deleted")


if students.find_one({"Name": "Nisha"}) is None:
    students.insert_one(student)
    print("One student data inserted successfully!")
else:
    print("Student already exists")

print("\nStudent Records:")
for stud in students.find():
    print(stud)


