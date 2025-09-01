name="Nisha"
message='hellooo everyoneee!'
multiline1 = """This is a multiline String"""
multiline2 = '''this is again a multiline string'''

print(name)
print(message)
print(multiline1)
print(multiline2)

#traversing in reverse order
for i in range(-1,-6,-1):
  print(name[i], end=" ")
print(end="\n")

#printing in ascending order
print(sorted(name,key=str.lower))

#printing in ascending order
print(sorted(name, key=str.lower ,reverse=True))

#traversing string 
for i in range(0,5,1):
  print(name[i], end=" ")
  
print(end="\n")
print(len(name))
print(name[1:5])
print(message[-18:-11])
print("Hello" + " world!")
print("Hi!" * 5)
print( "N" in name)

print(multiline1.find("String")) #20
print(multiline2.find("java")) #-1
print(multiline2.count("i")) # 6 count occurrences

fruits = "apple,banana,orange"
fruits1=(fruits.replace("banana","grapes"))
print(fruits1)
print(fruits)