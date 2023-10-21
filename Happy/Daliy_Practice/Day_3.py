

# check prime number

# def prime(num):
#     if num==1:
#         print("Not Prime")
#     else:
#         for i in range(2,num):
#           if num%i ==0:
#              print("not prime")
#              break
#         else:
#             print("prime")
#
#
# prime(6)


n1=0
n2=1
sum=0

for i in range(1,10):
    print(sum)
    n1=n2
    n2=sum
    sum=n1+n2