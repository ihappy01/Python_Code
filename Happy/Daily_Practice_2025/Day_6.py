

# Decorator --working
#
# def greeting(fx):
#     def mfx(*args):
#         print("Good Morning jjj")
#         fx(*args)
#     return mfx
#
#
# @greeting
# def hello():
#     print("Hello World hh")
#
# @greeting
# def add(a,b):
#     print(a+b)
#
#
# hello()
#
# add(7,5)


# Variable argument --working

# def average(*num):
#     print(type(num))
#     sum=0
#     for i in num:
#         sum=sum+i
#
#     return sum/len(num)
#
# print(average(5,5,5))

# Variable argument as directory --working

# def show(**kwargs):
#     print(kwargs)
#     print("Hello",kwargs['a'],kwargs['b'],kwargs['c'])
#
#
# show(a=4,b=46,c=8)

# num = int(input("Enter the value of number: "))
# print(type(num))
#
# for i in range(num):
#     print(i)


# getter and setter

class Calculation:
    def __init__(self,value):
        self.value =value

    @property
    def ten_value(self):
        return self.value*10

    @ten_value.setter
    def ten_value(self,new_vale):
        self.value=new_vale/10

    def show(self):
        print(self.value)


a=Calculation(304)

a.ten_value=76
print(a.ten_value)
a.show()






