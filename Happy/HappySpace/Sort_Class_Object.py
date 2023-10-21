class Fruit:
    def __init__(self,name,color,cost=0):
        self.name =name
        self.color =color
        self.cost = cost

    def __str__(self):
        return f"{self.name} - {self.color} {self.cost}"

def sort_by_cost(f):
    f.name

fruits = [ Fruit('apple','red',1.5),Fruit('banana','yellow','3.5'),Fruit('grape','purple',0.5)]

# from operator import attrgetter
#
# by_cost = list(sorted(fruits,key=attrgetter('cost')))


sorted_fruit = sorted(fruits,key=sort_by_cost)
for fruit in by_cost:
    print(fruit)