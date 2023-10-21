

# class Math:
#     def __init__(self,a,b):
#         self.a=a
#         self.b=b
#
#     def div(self):
#         print(self.a/self.b)
#
#     def mul(self):
#         print(self.a*self.b)
#
#
# ob=Math(6,7)
#
# ob.div()
# ob.mul()

# ==============================

# def gen_func():
#     for i in range(10):
#         yield i
#
#
# gen_obj= gen_func()
# print(next(gen_obj))
# print(next(gen_obj))
# print(next(gen_obj))


# -----------

# def prime(num):
#     if num==1:
#         print("not prime")
#     else:
#         for i in range(2,num):
#             if num%i==0:
#                 print("Not Prime")
#                 break
#         else:
#             print("Prime")
#
# prime(4)

# -------------------

# for i in range(1,20):
#     if i==1:
#         continue
#     else:
#         for j in range(2,i):
#             if i%j==0:
#                 break
#         else:
#             print(i)


# --------------------------

# n1=0
# n2=1
# next_num=0
#
# for i in range(1,11):
#     print(next_num)
#     n1=n2
#     n2=next_num
#     next_num=n1+n2


# ---------------------
#
# a=10
# b=20
# temp=0
#
# # temp=a
# # a=b
# # b=temp
#
# # a,b=b,a
# print(a , b)


# ---------------------------

# st = "Hello World"
# # s=" "
# # for ch in st:
# #     s=ch+s
# #
# # print(s)
#
# # s=st.split(" ")
# # t=(s[::-1])
# print(' '.join(st.split(" ")[::-1]))
# st[::-1]
# print(st)
# print(" ".join(st))

# ---------------------

# text ="Hello World"
# word=text.split(" ")
# d={}
# d1={}
# # count=1
# for ch in text:
#     d[ch]=d.get(ch,0)+1
#
# for  in text:
#     d[ch]=d.get(ch,0)+1



# print(d)
# ----------------------

# def greeting(fx):
#     def mfx():
#         print("Hello World")
#         fx()
#         print("Hello, Good Evening")
#     return mfx
#
# @greeting
# def add():
#     print(5+8)
#
# add()


#======================
# l = [9,2,5,7,6,4]
#
# # def cube(i):
# #     return i*i*i
#
# # l1 = list(map(cube,l))
# l1 = list(map(lambda x: x*x*x,l))
# print(l1)

# ========================

# func = lambda x:x*x
#
# print(func(5))

l = [3,6,7]

l1=list(map(lambda x:x*x,l))
print(l1)