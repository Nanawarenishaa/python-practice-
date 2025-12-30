

class Student:
    def __init__(self,f_name,l_name,qualification):
        self.f_name=f_name
        self.l_name=l_name
        self.qualification=qualification

    def update_Qualification(self,Q):
        self.qualification=Q

    def display(self):
        print("Student First Name:",self.f_name)
        print("Student Last Name:",self.l_name)
        print("Student qualification:",self.qualification)

S=Student("Nisha","Nanaware","BCA")

print("\nStudent Info:")
S.display()

print("\nStudent Info After Updation:")
S.update_Qualification("MCA")
S.display()
