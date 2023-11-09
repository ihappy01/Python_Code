

class Employee:
    def setName(self,nm):   # setter method
        self.name = nm


    def getName(self):      # getter method
        print("The name of the employee is ",self.name)


e1= Employee()
e2= Employee()

e1.setName(input("Enter the Employee Name:"))
e2.setName(input("Enter the Employee Name:"))
print(e1.__dict__)
print(e2.__dict__)
e1.getName()
e2.getName()