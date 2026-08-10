l1  = [3,5,2,7,1,67,44,55,77,89,24,0]
l2  = [4,8,2,9,5,6,67,33,0]

#
l3 = []

for x in l1:
    for y in l2:
        if y == x:
            l3.append(y)

# print(l3)


# l3  = list(set(l1) & set(l2))
# print(l3)

cl = [y for x in l1 for y in l2 if y==x]
print(cl)



