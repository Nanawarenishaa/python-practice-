matrix = []
rows = int(input("Enter rows you want: "))
cols = int(input("Enter cols you want: "))

for i in range(rows):
    L=[]
    for j in range(cols):
       t=int(input("Enter value: "))
       L.append(t)
    matrix.append(L)

print("Original Matrix:")
for i in matrix:
    print(i)

rows1 = []
cols1 = []
values = []
 
for i in range(rows):
    for j in range(cols):
        if matrix[i][j] != 0:
            rows1.append(i)
            cols1.append(j)
            values.append(matrix[i][j])

print("Sparse matrix triplet:")
print("Rows: ",rows1)
print("Cols: ",cols1)            
print("Non-zero values: ",values)
print("Addition of values: ", sum(values))
print("Max in values: ", max(values))