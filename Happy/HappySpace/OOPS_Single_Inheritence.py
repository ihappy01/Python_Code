
class HumanBeing:
    def __init__(self,name):
        self.name =name
        print("The Human Being Constructor is called")

class Employee(HumanBeing):
    def __init__(self,name,salary):
        super().__init__(name)
        self.salary=salary
        print(f"{self.name} is earning {self.salary} amount")


e1= Employee("Muskan",20000)