from time import perf_counter


class Employee:
    def __init__(self,name,id):
        self.name = name
        self.id = id

    def display(self):
        print(f"The employee {self.name} has {self.id} id")


e1= Employee("Shubham",78)
e1.display()

class Manager(Employee):

    def __init__(self,name,id,role):
        super().__init__(name,id)
        self.role = role

e2 = Manager("Indrajeet",89,"Manager")

e2.display()
# print(e2.__dir__())

l=[4,5,74,3]
print(dir())

# Static method

class Math:
    def __init__(self,num):
        self.num = num

    def addtonum(self,n):
        self.num = self.num+n

    @staticmethod
    def add(a,b):
        return a+b

m=Math(10)

print(m.num)
(m.addtonum(78))
print(m.num)

print(m.add(7,9))





# class Employee:
#     def __init__(self):
#         self.__name="Indrajeet"
#
# e=Employee()
# # print(e.__name)
# print(e._Employee__name)

s= "indrajeet happy"

# st =s.split(" ")
# print(f"{st[0][0].upper()+st[0][1:]} {st[1][0].upper()+st[1][1:]}")
# # print(st[1][0].upper()+st[1][1:])

# print(s.capitalize())

# Generator

def num():
    for i in range(5):
        yield i


o=num()
# print(next(o))
# print(next(o))
# print(next(o))
# print(next(o))
# print(next(o))

# for j in o:
#     print(j)


n = (x for x in range(6))
print(next(n))


