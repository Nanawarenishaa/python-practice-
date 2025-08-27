class employee:
    def __init__(self, name="Harry" , age=32 , department= " Computer science " ):
        self.name = name
        self.age = age
        self.department = department
    print(" Data of employee: ")
    print("Name      Age      Department")
    def display(self):
        print("--------------------------------")
        print(self.name, "|" , self.age , "|" , self.department)
        

emp1 = employee("Nisha",21," Data Science ")
emp2= employee()

emp1.display()
emp2.display()