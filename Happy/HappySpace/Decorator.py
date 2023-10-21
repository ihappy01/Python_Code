"""
A decorator is a function that takes another function as an argument and returns a new function
that modifies the behavior of the original function. The new function is often reffered to as a
"decorated" function. The basic syntax for using decorator is the following

@decorator_function
def my_function():
    pass
"""


# def greet(fx):
#     def mfx(*args, **kwargs):
#         print("Good Morning")
#         fx(*args, **kwargs)
#         print("Thanks for using this function")
#
#     return mfx
#
#
# @greet
# def hello():
#     print("Hello World")
#
#
# @greet
# def add(a, b):
#     print(a + b)
#
#
# # greet(hello)()
# # hello()
#
# add(7,8)



def greet(fx):
    def mfx(*args,**kwargs):
        print("Good Morning")
        fx(*args,**kwargs)
        print("Thanks for using the function")
    return mfx

@greet
def hello():
    print("Hello World")

@greet
def add(a,b):
    print(a+b)

add(54,46)


# hello()



