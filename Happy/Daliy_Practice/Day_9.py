
# def greeting(fx):
#     def mfx():
#         print("Hello , Good Morning")
#         fx()
#         print("Hello, Good Evening")
#     return mfx
#
# @greeting
# def add():
#     print(5+9)
#
#
# a=add()

# ================================

# def check_generator(num):
#     for i in range(num):
#         # yield f"Next number is {i}"
#           yield i
#
# gen_obj=check_generator(19)
# print(type(gen_obj))
# print(next(gen_obj))
# print(next(gen_obj))
# print(next(gen_obj))
# print(next(gen_obj))
# print(next(gen_obj))
# # print(next(gen_obj))


# ===================
# def gen():
#     for i in range(10,20):
#         if i==1:
#             continue
#         else:
#             for j in range(2,i):
#                 if i%j ==0:
#                     break
#             else:
#                 yield (i)
#
# gen_obj= gen()
#
# print(next(gen_obj))
# print(next(gen_obj))
# print(next(gen_obj))


# ----------------

# def prime(num):
#     if num==1:
#         print("NUM is not prime")
#     else:
#         for i in range(2,num):
#             if num%i==0:
#                 print("Num is not prime")
#                 break
#         else:
#             print("Num is prime")
#
#
# prime(1)

# ====================

n1=0
n2=1
next_num=0

for i in range(1,10):
    print(next_num)
    n1=n2
    n2=next_num
    next_num=n1+n2