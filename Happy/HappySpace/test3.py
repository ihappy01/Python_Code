l = [34, 3, 56, 7, 35, 55,100, 24, 98]

max = l[0]
sec_max = l[0]

for i in l:
    if i>max:
        max=i
    elif i>sec_max and i!=max:
        sec_max=i

print(sec_max)
# Not working
# for i in l:
#     if (i>max):
#         max=i
#     if(max2>max):
#         max=max2

#Working
# l.sort()
# print(l[-2])

# print(sorted(l)[-2])

# l1=sorted(l)
# print(l1)


