

mylist = [18,-3,5,0,-1,12,-9]

l = [x for x in mylist]
print(l)

# l = [abs(x) for x in mylist]
# print(l)

l1 = [(x*-1) if x<0 else x for x in mylist ]
print(f'the list after updating absolute value {l1}')
