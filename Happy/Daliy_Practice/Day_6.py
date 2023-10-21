

l= [4,2,5,8,9]

l1=list(map(lambda x:x*x,l))
print(l1)

l2 = list(filter(lambda x:x>2,l))

print(l2)

from functools import reduce
l3 = list(reduce(lambda x,y: x+y, l))
print(l3)