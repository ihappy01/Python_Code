
# def greeting(fx):
#     def mfx(a,b):
#         print("Hello,Good Morning All")
#         fx(a,b)
#     return mfx
#
# @greeting
# def add(a,b):
#     print(a+b)
#
# add(5,7)


# ==============

# l=[2,3,4,6]
# s = list(map(lambda x:x*x,l))
# print(s)

# l=lambda x:x*x
#
# print(l(5))

l = [1, 1, 2, 2, 3, 3, 4, 4, 67, 8, 9, 0, 0, 0]

d={}

for i in l:
    d[i]=d.get(i,0)+1

print(list(d.keys()))
