

l = [34,56,12,23,76,93,47,86]

# l.sort()
#
# print(l)
# print(f"Second largest number is {l[-2]}")

# n= len(l)
#
# for i in range(n):
#     for j in range(n-i-1):
#         if l[j]>l[j+1]:
#             l[j],l[j+1]=l[j+1],l[j]
#
#
# print(l)

max=l[0]
sec_max=l[0]

for i in l:
    if i >max:
        sec_max=max
        max=i
    elif i >sec_max:
        sec_max=i


print(sec_max)


