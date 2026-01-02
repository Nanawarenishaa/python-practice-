def printEvenOdd(s):
    str=list(s)

    for i in range(0,len(s)-1,2):
        str[i],str[i+1]=str[i+1],str[i]
        
    return "".join(str)   
char=input("Enter characters:")
print(printEvenOdd(char))