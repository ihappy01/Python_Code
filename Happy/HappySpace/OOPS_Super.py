

class Person:
    def __init__(self,name,age):
        self.name=name
        self.age=age
        print("Person Constructor called")

    def method(self):
        print("Person Method")
        print(f"{self.name} age is {self.age}")

class Employee(Person):
    def __init__(self,company,name,age):
        super().__init__(name,age)
        self.company=company
        print("Company constructor called")


    def method_emp(self):
        print("Employee Method")
        super().method()
        print(f"{self.name} works in {self.company}")



# p1 = Person("Indrajeet",20)
e1 = Employee("Sony","Shubahm",19)
# p1.method()
# e1.method_emp()
e1.method_emp()






