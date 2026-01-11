from pymongo import MongoClient

# 1. Connect to MongoDB
client = MongoClient("mongodb://localhost:27017")

# 2. Create / Select Database
db = client["bookdb"]

# 3. Create / Select Collection
books = db["Books"]

# 4. Insert 5 documents into Books collection
books.insert_many([
    {"Title": "Python", "Author": "Guido", "Publisher": "Pearson", "Price": 450},
    {"Title": "C++", "Author": "Guido", "Publisher": "BPB", "Price": 550},
    {"Title": "DSA", "Author": "Thomas", "Publisher": "Pearson", "Price": 750},
    {"Title": "Java", "Author": "James", "Publisher": "OReilly", "Price": 350},
    {"Title": "WebDev", "Author": "Guido", "Publisher": "Pearson", "Price": 850}
])

print("5 documents inserted successfully")

# i) Retrieve books whose publisher is 'Pearson'
print("\nBooks published by Pearson:")
for book in books.find({"Publisher": "Pearson"}):
    print(book)

# ii) Retrieve books whose price is between 400 and 600
print("\nBooks with price between 400 and 600:")
for book in books.find({"Price": {"$gte": 400, "$lte": 600}}):
    print(book)

# iii) Retrieve books in descending order of price
print("\nBooks in descending order of price:")
for book in books.find().sort("Price", -1):
    print(book)

# iv) Update the price of book by 10% whose title is 'Python'
books.update_many(
    {"Title": "Python"},
    {"$mul": {"Price": 1.10}}
)
print("\nPrice of Python books updated by 10%")

# v) Update the title of a book whose author is 'Guido' and publisher is 'BPB'
books.update_one(
    {"Author": "Guido", "Publisher": "BPB"},
    {"$set": {"Title": "Advanced C++"}}
)
print("Title updated successfully")

