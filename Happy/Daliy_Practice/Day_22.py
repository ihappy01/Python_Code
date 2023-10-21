
# def prime(num):
#     if num ==1:
#         print("Not Prime")
#
#     else:
#         for i in range(2,num):
#             if num%i==0:
#                 print("Not Prime")
#                 break
#         else:
#             print("Prime")
#
#
# prime(4)


n1=0
n2=1
next_num=0

for i in range(6):
    print(next_num)
    n1=n2
    n2=next_num
    next_num=n1+n2
