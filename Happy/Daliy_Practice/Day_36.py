from datetime import datetime

ob = datetime.now()
print(ob.strftime("%D %H:%M:%S"))
# Custom error handling
# class FiveDivisionError(Exception):
#     def __init__(self):
#         print("Division by 5 is not allowed")
#
#
# try:
#     a=int(input("Enter a number:"))
#     b=int(input("Enter a number:"))
#
#     if b==5:
#         raise FiveDivisionError
#
#     div=a//b
#     print(div)
# except (FiveDivisionError,Exception) as e:
#     print(e)


text = "My name is Indrajeet"
s=''

# for ch in text:
#     s=ch+s
# print(s)

# s=text.split(" ")
# l=[]
#
# for word in s:
#     l.append(word[::-1])
#
# print("The reverse of each word in sentence is:",' '.join(l))

# size=4
# l=len(text)
# i=0
#
# while i<l:
#     s=s+text[i:i+size][::-1]
#     i=i+size
#
# print(s)

# ch=list(text)
# left,right = 0,len(text)-1
#
# while left<right:
#
#     if ch[left]==" ":
#         left=left+1
#
#     if ch[right]==" ":
#         right=right-1
#
#     ch[left],ch[right]=ch[right],ch[left]
#
#     left=left+1
#     right=right-1
#
# print("Reverse of the sentence preserving space is:",("").join(ch))


l = [3,5,7,88,44,66,82,99]
# max=l[0]
# sec_max = l[0]
#
# for i in l:
#     if i>max:
#         sec_max=max
#         max=i
#     if i>sec_max and i!=max:
#         sec_max=i
#
#
# print(sec_max)

# a = [3,5,7,88,44,66,82,99]
# l = len(a)
#
# for i in range(l):
#     for j in range(l-1-i):
#         if a[j]>a[j+1]:
#             a[j],a[j+1]=a[j+1],a[j]
#
# print(a)