def reverse_words(char):
    words=char.split()
    reversed=[]

    for word in words:
         reversed.append(word[::-1])
    return " ".join(reversed)

string=input("enter sentence:")
print(reverse_words(string))




