
class HumanBeing:
    def __init__(self,name):
        self.name =name
        print("The Human Being Constructor is called")

class Employee(HumanBeing):
    def __init__(self,name,salary):
        super().__init__(name)
        self.salary=salary
        print(f"{self.name} is earning {self.salary} amount")

class Manager(Employee):
    def __init__(self,name,salary,bonus):
        super().__init__(name,salary)
        self.bonus = bonus
        print(f"{self.name} is the manager and his salary is {self.salary} and bonus is {self.bonus}")



m1= Manager("Shubham",100000,20000)