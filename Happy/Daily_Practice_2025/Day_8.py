
class Employee:
    company_name = "Apple"
    noOfEmployee = 0
    def __init__(self,name):
        self.name = name
        self.raise_amount = 0.02
        Employee.noOfEmployee = Employee.noOfEmployee+1

    def show(self):
        print(f"The name of the {Employee.noOfEmployee} Employee is {self.name} and the raise amount in {self.company_name} is {self.raise_amount}")


e1= Employee("Indrajeet")
# Employee.show(e1)
e1.raise_amount = .04
e1.company_name =  "Apple India"
e1.show()

Employee.company_name = "Google"
print(Employee.company_name)

e2= Employee("Shubham")
e2.company_name= "Nestle"
e2.show()
