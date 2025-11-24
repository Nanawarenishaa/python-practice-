class student:
    def __init__(self,marks):
        self.marks=marks

    def __gt__(self,other):
        return self.marks > other.marks
    
stud1=student(78)
stud2=student(77)
stud3=stud1>stud2
print(stud3)