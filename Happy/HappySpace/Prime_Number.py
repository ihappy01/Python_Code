# working code

def prime_num(num):
    if num==1:
        print("Number is not prime")
    else:
        for i in range(2,num):
            if num%i==0:
                print("The number is not prime")
                break
        else:
            print("Number is prime")

prime_num(6)

#==========================================
# Working code
# Program to print prime number
for i in range(10,30):
    if i==1:
        continue
    else:
        for j in range(2,i):
            if i % j==0:
             break
        else:
            print(i)




# =========================================================
# def prime(num):
#     if num > 1:
#
#         for i in range(2 ,num//2):
#             if num %2 ==0:
#                 print("Number is not prime")
#                 break
#             else:
#                 print("Number is prime")
#                 break
#     else:
#         print("Enter number greater then 1")
#
# prime (5)

# def prine(num):
#     if num==1:
#         print("Number is not prime")
#     elif num>1:
#         for i in range(2,int(num/2)+1):
#             if num%2==0:
#                 print("Number is not prime")
#                 break
#             else:
#                 print("Number is prime")
#                 break
#     else:
#         print("Enter number greater than 1")
#
# prine(3)

# 29 june 2023

# def prime(num):
#     if num<1:
#         print("Enter positive number")
#     elif num==1:
#         print("Number is not prime number")
#     else:
#         for i in range(2,int(num/2)+1):
#             if i%2==0:
#                 print("Number is not prime g")
#                 break
#             else:
#                 print("Number is prime")
#
# prime(11)

# def prime(num):
#     if num<1:
#         print("Enter positive number only")
#     elif(num==1):
#         print("Number is not prime ")
#     else:
#         for i in range(2,num):
#             if num%i==0:
#                 print("Not prime ")
#                 break
#         else:
#             print("The number is prime")
#
# prime(5)

# def prime(num):
#     if num<=1:
#         print("Number is  not prime")
#     else:
#         for i in range(2,int(num/2)+1):
#             if (num%i==0):
#                 print("Number is not prime")
#                 break
#         else:
#             print("The number is prime")
#
#
# prime(70)


