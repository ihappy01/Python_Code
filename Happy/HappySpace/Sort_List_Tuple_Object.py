# List
# li = [9,1,8,2,7,3,6,4,5]
#
# s_li = sorted(li)
#
# print("Sorted Variable:\t",s_li)
# li.sort(reverse=True)
# print("Original Variable:\t",li)


# Tuple
# tup =(9,1,8,2,7,3,6,4,5)
# s_tup = sorted(tup)   # return a list
# print("Tuple:\t",s_tup)

# Dictionary
#
# di = {'name':"Indrajeet",'job': 'programming', 'age':None,'os':'mac'}
# s_di = sorted(di)
# print("sorted dictionary:\t",s_di)
# print(di)

# li = [-6,-5,-4,1,2,3]
# s_li = sorted(li,key=abs)
# print(s_li)


class Employee:
    def __init__(self,name,age,salary):
        self.name =name
        self.age = age
        self.salary = salary

    def __repr__(self):
        return (f"({self.name} ,{self.age} , {self.salary})")
    # def __str__(self):
    #     return (f"({self.name} ,{self.age} , {self.salary})")

e1 = Employee('Carl',37,70000)
e2 = Employee('Sarah',29,80000)
e3 = Employee('Jhon', 43 , 90000)

employees = [e1,e2,e3]
#
# def e_sort(emp):
#     return emp.age

from operator import attrgetter
s_employees = sorted(employees,key=attrgetter('age'))
print(s_employees)
