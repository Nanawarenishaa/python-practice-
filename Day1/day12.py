from pymongo import MongoClient

client=MongoClient("mongodb://localhost:27017/")
print("connecting to mongodb..")

db=client["school"]
collection=db["students"]

print("connected to mongodb to successfully..")

student={
    "Name":"Nisha",
    "Course":"MCA"
    }

collection.insert_one(student)
print("records inserted successfully")

for doc in collection.find():
    print(f"Name:{doc['Name']} | Course:{doc['Course']}")

