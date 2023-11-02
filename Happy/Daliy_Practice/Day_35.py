# Reverse string preserving space

# text="I am python"
# text="My name is Indrajeet"
# s=list(text)
# l=len(text)
# left,right =0,l-1
#
# while left<right:
#     if s[left]==" ":
#         left=left+1
#
#     if s[right]==" ":
#         right=right-1
#
#     s[left],s[right] = s[right],s[left]
#
#     left=left+1
#     right=right-1
#
#
# print(''.join(s))

# Reverse String on substring basis

# text=("My name is Indrajeet kumar")
# i=0
# size=4
# l=len(text)
# s=''
#
# while i<l:
#     # sub=''
#     # r=text[i:i+size]
#     # for ch in r:
#     #     sub=ch+sub
#
#     s=s+text[i:i+size][::-1]
#     # s=s+sub
#     # print(text[i:i+size])
#     i=i+size
#
# print(s)


# User defined exception

# class FiveDivisionError(Exception):
#     def __init__(self):
#         print("Division by 5 is not allowed in this function")
#
#
# try:
#     a=int(input("Enter value of a:"))
#     b=int(input("Enter value of b:"))
#     if b==5:
#         raise FiveDivisionError
#     div=a/b
#     print(div)
# except (FiveDivisionError,Exception) as e:
#     print(e)

# Reverse word
# text="My name is Indrajeet"
# s=text.split()
# l=[]
# for word in s:
#     l.append(word[::-1])
# print(' '.join(l))


# Find occurrence of each element and the highest element
# text="My name is Indrajeeet"
# d={}
#
# # for ch in text:
# #     if ch in d:
# #         d[ch]=d[ch]+1
# #     else:
# #         d[ch]=1
#
# for ch in text:
#     d[ch]=d.get(ch,0)+1
#
# print(d)
# print(max(d,key=d.get))


# a= [3,4,5,2,6,1,7,6,0]
# l=len(a)
# target = 7
# b =[]
#
# for i in range(l):
#     for j in range(i+1,l):
#         if a[i]+a[j]==target:
#             b.append((a[i],a[j]))
#
# print(b)


# n1=0
# n2=1
# next_num=0
#
# for i in range(10):
#     print(next_num)
#     n1=n2
#     n2=next_num
#     next_num=n1+n2

def prime(num):
    if num==1:
        print("Not prime")
    else:
        for i in range(2,num):
            if num%i==0:
                print("Not Num")
                break
        else:
            print("Prime Num")

prime(5)

