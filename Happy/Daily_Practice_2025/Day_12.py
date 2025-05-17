# x= [1,2,3]
#
# print(dir(x))
#
# # t = (1,2,4)
# t = "(1,2,4)"
#
# print(dir(t))

class Person:
    def __init__(self,name,age):
        self.name = name
        self.age = age


p = Person("John",30)
p1 = Person("Harry",32)
print(p.__dict__)
print(p1.__dict__)

# print(help(str))
print(help(Person))