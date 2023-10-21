
text = "abcdabcdefgheacdefghd"
# method 1
# d={}
# for ch in text:
#     if ch in d:
#         d[ch]=d[ch]+1
#     else:
#         d[ch]=1
# print(d)

#Method 2
# d={}
# for ch in text:
#     d[ch]=d.get(ch,0)+1
#
# print(d)
# print(max(d,key=d.get))
#
# for key,value in d.items():
#     print(f"The count of {key} in text is {value} ")


# def prime(num):
#     if num==1:
#         print('not prime')
#     else:
#         for i in range(2,num):
#             if num%i==0:
#                 print("Not Prime")
#                 break
#         else:
#             print("Prime Number")
#
# prime(11)
# try:
#     # for i in range(10,20):
#     #     if i==1:
#     #         continue
#     #     else:
#     #         for j in range(2,i):
#     #             if i%j==0:
#     #                 break
#     #         else:
#     #          print(i)
#     l=[2,3,4]
#     print(l[9])
# # except Exception as e:
# #     print(e)
#
# except:
#     print("Error raised")


# def greeting(fx):
#     def mfx(num1,num2):
#         print("Hello Good Morning")
#         fx(num1,num2)
#     return mfx
#
# @greeting
# def add(a,b):
#
#     print("Hello Good Evening")
#     return print(a+b)
#
# add(6,7)
# # print(a)

# def num():
#     for i in range(10):
#         yield i
#
# gen_ob=num()
# print(next(gen_ob))
# print(next(gen_ob))
# print(next(gen_ob))

# d= lambda x:x*x
# print(d(5))

l=[9,8,5,3]
print(list(map(lambda x:x*x,l)))


