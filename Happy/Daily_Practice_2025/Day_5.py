from audioop import reverse
from tkinter.font import names

# print("Hello world")
#
# class Employee:
#     def __init__(self,name,ID):
#         self.name = name
#         self.ID = ID
#
#
# a = Employee("Indrajeet",20)
#
# print(a.name)
# print(a.ID)

# for i in range(5,10):
#     print(i,end=" ")
#
# l= ['a','b','c','d','f']
# print("\n")
# for ch in l:
#     print(ch)

# Create a math class.Initialize 2 attributes as x and y . Define 2 methods- division and multiplication.
# Create object. Call both methods for that object.

class Math:
    x=10
    y =5

    def division(self):
        return self.x/self.y

    def multiple(self):
        return self.x*self.y


obj = Math()
div_val=obj.division()
print(div_val)
mul_val=obj.multiple()
print(mul_val)

#=======================

s = "Hello Wolrd"
rev=''
for ch in s:
    rev=ch+rev

print(rev)

print(s[::-1])

# for ch in reversed(s):
#     print(ch,end='')

print(list(reversed(s)))

print("".join(reversed(s)))



