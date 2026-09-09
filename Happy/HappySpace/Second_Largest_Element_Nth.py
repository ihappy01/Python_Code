l = [34, 3, 56, 7, 35, 55,100, 24, 98]

#==============================
# second largest without using sort
max=0
sec_max =0


for i in l:
    if i>max:
        sec_max=max
        max=i
    elif i>sec_max and i!=max:
        sec_max=i

print(sec_max)




#===================================================
# 3rd largest without using sort
# max=l[0]
# sec_max =l[0]
# third_max=l[0]
#
# for i in l:
#     if i>max:
#         third_max=sec_max
#         sec_max=max
#         max=i
#     elif i>sec_max and i!=max:
#         third_max=sec_max
#         sec_max=i
#     elif i>third_max and isec_max and i!=third_max:
#         third_max=i
#
# print(sec_max)
# print(third_max)

# =======================================

# length=len(l)
#
# for i in range(length):
#     for j in range(length-1):
#         if l[i]<l[j]:
#           l[i],l[j]=l[j],l[i]
#
#
# print(l[-2])



