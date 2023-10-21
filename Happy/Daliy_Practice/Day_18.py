# names = ["John", "Mary", "Peter"]
#
# upper_name = list(map(str.upper,names))
# lower_name = list(map(str.lower(),names))
#
# print(lower_name)
# print(upper_name)
# ------------------

# def greeting(fx):
#     def mfx():
#         print("Hello good Morning")
#         fx()
#     return mfx
#
# @greeting
# def add():
#     print(5+8)
#
# add()
l=[4,5,6]

t = list(map(lambda x:x*x,l))

print(t)