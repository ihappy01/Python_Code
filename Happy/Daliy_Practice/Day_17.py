
# ======================
text="aabbbccccddaaaaa"

# s=""
# l=len(text)
# count=1
# for i in range(l-1):
#     if text[i]==text[i+1]:
#         count=count+1
#     else:
#         s = s+text[i]+str(count)
#         count=1
#
# s =s+text[i]+str(count)
#
# print(s)
# ============================


# input is 1,2

'''
(1,)
(2,)
(3,)
(1, 2)
(1, 3)
(2, 3)
(1, 2, 3)
'''
# from itertools import combinations
#
# # print(list(combinations('123',2)))
# l= [1,2,3]
#
# for i in range(1,4):
#     combs = combinations(l,i)
#     for comb in combs:
#         print(comb)


# ================


# str = "azyb"

# # a=z z=b ,y=a b=y
#
# char ={'a':'z','z':'b','y':'a','b':'y'}
# s=""
# for ch in str:
#     if ch in char:
#         s=s+char[ch]
#
# print(s)

# ======================
# Reverse half string
# str = "azyb"
# output "zaby

# str ="asdfgh"
# s1  = str[:2:-1]
# s2 = str[2::-1]
# print(s1)
# print(s2)
# print(s2+s1)

# def reverse_from_half(input_str):
#     length = len(input_str)
#     mid = length // 2  # Find the midpoint of the string
#
#     first_half = input_str[:mid]  # Extract the first half
#     second_half = input_str[mid:]  # Extract the second half
#
#     reversed_str = first_half[::-1] + second_half[::-1]  # Reverse both halves and combine
#
#     return reversed_str
#
# # Example usage
# input_str = "azybghjk"
# output = reverse_from_half(input_str)
# print(output)
# -----------------

# str = "qwertyuiopasdfghjklzxcvbnm"
#
# print(str[2::3])

# ------------------------
# 5. Write a program to combine 2 list as a dictionary.
# Write a program to combine 2 list as a dictionary.
l= ['a','b','c','d']
l1 = [1,2,3,4,5]

# print(dict(zip(l,l1)))
# print(tuple(zip(l,l1)))
# print(list(zip(l,l1)))
# d={}
# for key,value in zip(l,l1):
#     d[key]=value
#
# list=[]
# for key,value in zip(l,l1):
#     list.append([key,value])
#
# # print(d)
# # print(list)
#
# list = [[v1,v2] for v1,v2 in zip(l,l1)]
# print(list)

# l.insert(2,1)
# print(l)
# print(l+l1)
# l.extend(l1)
# print(l)
# print(l1)
#
# l= ['a','b','c','d']
# l1 = [1,2,3,4,5,6,7,8,9,6,0,1,2,3,4,6]
# l2=l.copy()
# print(l2)
# l2.pop()
# print(l)
# print(l2)
# l.remove()
# l.pop(2)
# print(l)
# print(l1.index(6,10,18))
# print(l)
# l.reverse()
# l.sort()
# print(l)

l= ['a','b','c','d']

for i,v in enumerate(l):
    print(i, v)
