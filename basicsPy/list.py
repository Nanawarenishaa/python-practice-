list = [ "Apple" , "banana" , "cherry " ]
list.append("grapes")
print(list)
list.remove("banana")
print(list)

numbers=[1,2,3,4]
print(len(numbers))  #4
print(len(numbers)-1) #3
print(min(numbers))  #1
print(max(numbers))  #4
print(sum(numbers))  #10
print(5 in numbers)  #false
numbers[3]=5 # assign 5 at the 3rd index [1, 2, 3, 5]
print(numbers)
numbers.pop(3) # delete ele from specific index or last ele [1, 2, 3]
print(numbers)
numbers.insert(4,6) # insert element at specific index
print(numbers)
numbers.extend([5,4,7])
print(numbers)
numbers.clear()   # empty list
print(numbers)
del numbers  # destroy list