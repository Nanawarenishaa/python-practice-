class student:
    def __init__(self,Fname,Lname,qualification):
        self.Fname=Fname
        self.Lname=Lname
        self.qualification=qualification

    def update_qualification(self,new_qualification):
        self.qualification=new_qualification

    def display_detail(self):
        print("Student First Name:",self.Fname)
        print("Student Last Name:",self.Lname)
        print("Student qualification:",self.qualification)

s1=student("Nisha","Nanaware","BCA")

print("Student detail:")
s1.display_detail()

print("updating qualification:")
s1.update_qualification("MCA")


print("updated Student detail:")
s1.display_detail()   