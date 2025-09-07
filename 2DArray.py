num = [
    [ 1, 2, 3],
    [ 4, 5, 6],
    [ 7, 8, 9]
]

for row in num:
    for col in row:
        print(col, end=" ") 
    print()

print("Odd numbers: ")
print(num[0][0])
print(num[0][2]) 
print(num[1][1])
print(num[2][0])
print(num[2][2])
print("Even numbers:")
print(num[0][1])
print(num[1][0])
print(num[1][2])
print(num[2][1])