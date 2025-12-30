rows=int(input("Enter rows:"))
cols=int(input("enter cols:"))

m=[]

for i in range(rows):
    row=[]
    for j in range(cols):
        row.append(int(input("Enter value:")))
    m.append(row)

r1=[]
c1=[]
value=[]
Sum=0
for i in range(rows):
   
    for j in range(cols):
        if m[i][j]!=0:
          r1.append(i)
          c1.append(j)
          value.append(m[i][j])
          Sum=Sum+m[i][j]

print("display matrics:")
for k in m:
    print(k)

print("Sparse Matrics:")
print("Rows:",r1)
print("colomns:",c1)
print("volues:",value)
print("sum of values:",Sum)
    
 
    
