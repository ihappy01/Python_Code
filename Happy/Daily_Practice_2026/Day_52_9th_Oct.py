# Input: d = {}
# 	     l = [1,2,3,4]
# 	    n= 10
# output:  d = {1: 10, 2:10,, 3:10, 4:10}
from itertools import repeat

d = {}
l = [1,2,3,4]
n= 10

# Method 1
# for i in l:
#     d[i]=n
# print(d)

#Method 2

m2= dict.fromkeys(l,n)
print(m2)

#method 3

m3 = {i:n for i in l}
print(m3)

#Method 4
m4 = dict(zip(l,repeat(n)))
print(m4)

d1= [2,4,6,8,10,12,14]
d2 =['a','b','c','d','e','f']

df = dict(zip(d1,d2))
print(df)

de = dict(enumerate(d2,1))
print(de)

