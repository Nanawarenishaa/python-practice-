dict = {
    "name" : "Nisha" ,
    "age" : 21 ,
    "program" : "MCA"
}

print("Student: ",dict)
print("Name: ", dict["name"])

dict["age"] = "22"
print("After modification: " , dict)

dict["city"] = "Pune"
print(" After adding city: ",dict)