'''
Step 1: Create an exception class and inherit from base Exception class. i.e Exception.
class InvalidAge(Exception):
    pass
Step 2: Raise InvalidAge exception for particular condition(age<0) inside try block
try:
    if age<0:
        raise InvalidAge("message"
Step 3: Handle the exception using except block.
except Exception as e:
    print(e)

'''

# Write a  python program for FiveDivisionError Exception.

class FiveDivisionError(Exception):
    "This is exception class called when five division error happen"
    def __init__(self):
        print("Cannot divide by Five",end="")

try:
    n1=int(input("Enter first number:"))
    n2=int(input("Enter second number:"))
    if n2==5:
        raise FiveDivisionError
    div=n1/n2
    print(div )
except (FiveDivisionError,ZeroDivisionError) as e:
    print(e)

print("Rest of the code")