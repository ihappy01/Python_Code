from email.policy import strict
from enum import STRICT

l =  {'Name','Age','Skill'}
l1 = {'Shubham',27,'Maths','Reasoning'}

d = dict(zip(l,l1))
# d = dict(zip(l,l1,strict=True))
print(d)

d1 = {'Color':'Red'}

# d.update(d1)
# print(d)

rd={}
# rd ={**d,**d1}
rd = d | d1
print(rd)





