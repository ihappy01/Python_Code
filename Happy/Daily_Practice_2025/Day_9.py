#----class method---Working
# class Employee:
#     company = "Apple"
#
#     def show(self):
#         print(f"The name is {self.name} and company is {self.company}")
#
#     @classmethod
#     def changeCompany(cls,newCompany):
#         cls.company = newCompany
#
#
#
# e1 = Employee()
# e1.name = "Indrajee"
# e1.show()
#
# e1.changeCompany("Sumsung")
# e1.show()
# print(Employee.company)

# --------------------

class Employee:
    def __init__(self,name,salary):
        self.name = name
        self.salary = salary

    @classmethod
    def fromstr(cls,st):
        return cls(st.split('-')[0],int(st.split('-')[1]))


e= Employee("Indrajeet",12000)
print(e.name)
print(e.salary)

st = "Harry-12200"

e2 = Employee.fromstr(st)
print(e2.name)
print(e2.salary)