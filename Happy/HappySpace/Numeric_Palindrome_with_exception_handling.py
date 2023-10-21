# num = 1234
# s=""
# for i in num:
#  print(i)

#=======================================
# try:
#     num = 1234
#     s=""
#     for i in num:
#         print(i)
# # except TypeError:
# #     print("TypeError Exception raise")
# except Exception as e:
#     print(e)
#
# print("Some important line of code")
# print("End of Program")
#=========================

# try:
#     raise Error
# except:
#     print("error raised")

try:
    raise NameError('Hi There')
# except Exception as e:
#     print(e)
except NameError:
    print("An exception flew by!")
    raise
finally:
    print("Goodbye world")


