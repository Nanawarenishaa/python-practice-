n = int(input("Enter number of elements: "))
my_set = set()


for i in range(n):
    element = input("Enter element (0-9 or A-Z or a-z): ")
    my_set.add(element)


print("\nSet elements:", my_set)

print("Length of set:", len(my_set))


digits = 0
lowercase = 0
uppercase = 0

for ch in my_set:
    if ch.isdigit():
        digits += 1
    elif ch.islower():
        lowercase += 1
    elif ch.isupper():
        uppercase += 1

print("Number of digits:", digits)
print("Number of lowercase letters:", lowercase)
print("Number of uppercase letters:", uppercase)
