

class Employee:
    company ="HCL"

    def __init__(self,name,id):
        self.name=name
        self.id=id

    def display(self):
        print(f"{self.name} is working in {Employee.company} and is having ID {self.id}")

    def change_name(self):
        self.name =input("Enter the name of the employee:")

    @classmethod
    def change_company(cls):
        cls.company="Persistent"



e1=Employee("INDRAJEET",4)
print(e1.__dict__)
e1.display()
e1.change_name()
e1.change_company()
e1.display()
print(Employee.__dict__)
