
l = [2,3,4,6,7,8,34,57,22,58,13,14,17]


max_ele=l[0]
sec_max_ele=l[0]

for i in l:
    if i > max_ele:
        sec_max_ele=max_ele
        max_ele=i
    elif i> max_ele and i< sec_max_ele:
        sec_max_ele=i


print(sec_max_ele)
