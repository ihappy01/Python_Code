

d = {x:x*x for x in range(2,5)}

print(d)

d1 =("abc","def","ghi")
d2=['a','b','c']

# d={}
# for k,v in zip(d1,d2):
#     d[k]=v
#
# print(d)
#
# d.pop('abc')
# print(d)
#
# d.popitem()
# print(d)

for key,value in d.items():
    print(f"{key} : {value}")

if 3 in d:
    print("Key EXITS")


d1 = {'a':1,'b':2,'c':3}
d2 = {'d':4,'e':5}

# m
# d1.update(d2)
# print(d1)
# print(d2)
#
# merged_dict = {**d1,**d2}
# print(merged_dict)

merge_dic= d1.copy()
#
for k,v in d2.items():
    merge_dic[k]=v
#
print(merge_dic)

