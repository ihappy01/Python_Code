"""
When a class contain two or more methods with same name but
different behaviour it is called Method overloading

Python does not support method overloading. It returns the behaviour of the latest method

"""

class Addition:
    def add(self,a,b):
        print(a+b)

    def add(self,c,d,e):
        print(c+d+e)


ob=Addition()
# ob.add(4,7)  # This call gives error that one argument is missing
ob.add(8,8,9)


"""
Indirectly we can write logic to achieve method overloading
"""

class Calc:
    def sum(self,a=None,b=None,c=None):
        if a!=None and b!=None and c!=None:
            print("Sum is:",a+b+c)
        elif  a!=None and b!=None:
            print("Sum is:",a+b)
        else:
            print("Incorrect number of argument")

c1=Calc()
c1.sum(10,20)
c1.sum(23,45,33)
