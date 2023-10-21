

class Person:
    def __init__(self,name,age):
        self.name = name
        self.age = age

    def per_method(self):
        print(f"The person name is {self.name} and age is {self.age}")


class Employee(Person):
    def __init__(self,name,age,salary):
        super().__init__(name,age)
        self.salary = salary

    def emp_method(self):
        print(f"The employee name is {self.name} and age is {self.age} and his salary is {self.salary}")


class Student(Person):
    def __init__(self,name,age,mark):
        super().__init__(name,age)
        self.mark = mark

    def std_method(self):
        print(f"The student name is {self.name} and age is {self.age} and his marks is {self.mark}")


e1 = Employee("Shubham",25,100000)
s1 = Student("Riya",20,70)

e1.emp_method()
s1.std_method()


