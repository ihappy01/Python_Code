'''
Instance Variable
Variables made for particular instance.
Separate copy is created for every object
Values of variables differs from object to object
Modification in once object won't effect other objects

Creating instance variables
-Using Constructor
-Using instance method
-Outside class
'''
# class Student:
#     def __init__(self,nm,m):
#         self.name=nm
#         self.marks=m
#
#     def dispaly(self):
#         print(f"The name of student is {self.name} and his/her score is {self.marks}")
#
#     def change_data(self):
#         self.name = input("Enter the name:")
#         self.marks = input("Enter the marks:")
#
#
# std1= Student("Akshay",98)
# std2= Student("Indrajeet",84)
# std3= Student("Shubham",88)
# std1.age =21
# std2.name="Happy"
#
# print(std1.__dict__)
# print(std2.__dict__)
# print(std3.__dict__)
#
# std3.change_data()
#
# std3.dispaly()
#

'''
Class Variables
-Variables made for entire class(All Objects)
-Only one copy is created and distributed to all objects
-Modification in class variable impact on all objects

Class Method
-Method which works on class variables
-First argument is class reference

'''

class Employee:
    company_name = "HCL"
    def __init__(self,nm,sal):
        self.name=nm
        self.salary=sal

    @classmethod
    def get_comapany_name(cls):
        cls.company_name='TCS'
        print(cls.company_name)

e1=Employee("Nikhil",100000)
e2=Employee("Shiv",150000)
print(e2.company_name)
# Employee.company_name = "Lnt"
# e1.company_name = "Mindtree"
# print(e1.__dict__)
# print(Employee.company_name)
# Employee.get_comapany_name()
