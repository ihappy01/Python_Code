
'''
The except block is executed when exception is raise
The else block is executed when exception is not raised
Either of except or else will be executed once
else and finally block are optional
We can have multiple except block for one try block
Finally block is always executed
except block : if exception
else block : if no exception

raise statement is used when we want to throw an exception for a particular condition

'''
import sys

# try:
#     a = int(input("Enter a number: "))
#     print(f"The multilpication of {a} is")
#
#     for i in range(1, 11):
#         print(f"{i} *{a} = {a * i}")
# except:
#
#     print("Invalid Input")
#
# print("Some important line of code ")
# print("End of program")


# try:
#     num =int(input("Enter a interger: "))
#     a=[6,3]
#     print(a[num])
# except ValueError:
#     print("Number is not valid Interger")
# except IndexError:
#     print("Index error")


# a=int(input("Enter 1st number:"))
# b=int(input("Enter 2nd number:"))
# try:
#     print(a/b)
# # except (ZeroDivisionError,NameError) as e:
# #     print(e)
# # except Exception as e:
# #     print(e.__class__)
# except:
#     print(sys.exc_info()[1])
# else:
#     print("Exception did not occur")
# finally:
#     print("Always executed")
#
# print("Rest of the code")

try:
    age =int(input("Enter your age:"))
    if age<0:
        raise ValueError("Invalid age")
    print("Age is:",age)

except ValueError as e:
    print(e)

print("Rest of the code")