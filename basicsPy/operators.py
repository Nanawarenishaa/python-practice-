# logical operators 

x = 10
y = 15
z = 20

# and operator
print( x < y and x < z) # both condition true
print( x > y and z > x )  # false because 10 > 15 is false

# or operator
print( x > y or z > x) # true because one condition (20 > 10) is true
print( x > y or x > z) # false because both conditions are false

# not operator
print(not(y > x))  # False because (15 > 10) is True, but NOT makes it False
print(not(y < x))   # True because (10 < 5) is False, and NOT makes it True