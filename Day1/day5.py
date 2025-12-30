r = int(input("Enter rows: "))
c = int(input("Enter columns: "))

m = []
print("Enter matrix elements:")
for i in range(r):
    row = []
    for j in range(c):
        row.append(int(input()))
    m.append(row)

print("Matrix:")
for row in m:
    print(row)

rows = []
cols = []
values = []

for i in range(r):
    for j in range(c):
        if m[i][j] != 0:
            rows.append(i)
            cols.append(j)
            values.append(m[i][j])

print("Sparse Matrix Representation:")
print("Row index:", rows)
print("Column index:", cols)
print("Values:", values)
