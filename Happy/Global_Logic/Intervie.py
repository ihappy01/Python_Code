


# def mul(fx):
#     def mfx(a,b):
#         print(a*b)
#         fx(a,b)
#         print("The multiplication operation is performed ")
#     return mfx
#
# @mul
# def fx(a,b):
#     print(a+b)
#
# fx(5,6)
# # mul(fx)(5,6)


# input is 1,2

'''
(1,)
(2,)
(3,)
(1, 2)
(1, 3)
(2, 3)
(1, 2, 3)
'''

from  itertools import combinations
l=[1,2,3]

# Generate all possible combination of number
for i in range(1,len(l)+1):
    combs = combinations(l,i)
    for com in combs:
        print(com)

# l = [1,2,3]
#
# for i in range(1,4):
#     for j in range(1,4):
#      print(i,j)



