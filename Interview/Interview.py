# class Aminal -Name , no_leg_legs,color

class Animal:
    def __init__(self,name,no_of_legs,color):
        self.name = name
        self.no_of_legs = no_of_legs
        self.color = color

    def display(self):
        print(f"{self.name} is having {self.no_of_legs} legs and its color is {self.color}")
class Dog(Animal):
    pass
class Cat(Animal):
    pass

ob =Dog("dog",4,"Golden")
ob1 = Cat('cat',4,'Black')

ob.display()
ob1.display()




input_list = ["3", "6", "2", "9", "4", "6"]

l=[]
for i in input_list:
    if i not in l:
        l.append(i)
print(l)

length = len(l)

for i in range(length):
    for j in range(length-i-1):
        if l[j]>l[j+1]:
            l[j],l[j+1]=l[j+1],l[j]

print("The sorted list is",l)