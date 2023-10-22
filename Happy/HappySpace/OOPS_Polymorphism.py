
# Polymorphism in python is an ability of python object to take many forms
# If a variable,method or object performs different behaviours according to situation is called as polymorphism
# + operator , len function , reversed function

'''
emp =["ram","jadu","madhu"]
company ="Persistent"

for i in reversed(emp):
    print(i)

for i in reversed(company):
    print(i)
'''
# Polymorphism example with inheritance

class Veh:
    def __init__(self,name,color,price):
        self.name = name
        self.color= color
        self.price = price


    def get_details(self):
        print("Name is",self.name)
        print("Color is",self.color)
        print("Price is",self.price)

    def max_speed(self):
        print("Maximum speed limit is 100")

    def gear(self):
        print("No of gear is 5")


class Car(Veh):
    def max_speed(self):
        print("Maximum speed limit is 140")

    def gear(self):
        print("No of gear is 6")

v1 = Veh("Truck","Red",1000000)
c1 = Car("Maruti","White",340000)

c1.max_speed()
c1.gear()



