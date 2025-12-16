s = input("Enter a string: ")
lst = list(s)

for i in range(0, len(lst) - 1, 2):
    lst[i], lst[i+1] = lst[i+1], lst[i]

result = "".join(lst)
print("Output string:", result)
