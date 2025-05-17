

class Person():
    def __init__(self,name,age):
        self.name=name
        self.age=age

    def person_method(self):
        print(f"The person name is {self.name} and age is {self.age}")


class Employee(Person):
    def __init__(self,name,age,salary):
        super().__init__(name,age)
        self.salary=salary

    def emp_method(self):
        print(f"The name of the person is {self.name} and age is {self.age} with salary {self.salary}")


p1=Person("Indrajeet",32)
e1=Employee("Shubham",28,50000)

e1.emp_method()
e1.person_method()