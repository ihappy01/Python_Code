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


try:
    num =int(input("Enter a interger: "))
    a=[6,3]
    print(a[num])
except ValueError:
    print("Number is not valid Interger")
except IndexError:
    print("Index error")