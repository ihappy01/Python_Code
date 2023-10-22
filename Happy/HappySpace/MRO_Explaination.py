'''
 Method Resolution Option represents how properties(attribute & methods) are searched in inheritance.
-Rule 1: Python first searches in the child class and then goes to the parent class. Priority is given to child class.
-Rule 2: MRO follows: 'Depth First Left to Right Approach'
-Rule 3:  You can use mro() method for knowing mro of any objects
'''

class A:
    pass

class B:
    pass

class C:
    pass

class X(A,B,C):
    pass

class Y(B,C):
    pass
class P(X,Y):
    pass

print(P.mro())
