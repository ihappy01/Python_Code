# from itertools import combinations
#
# l =[1,2,3]
#
# print(list(combinations(l,1)))

# for i in range (1,len(l)+1):
#     for comb in combinations(l,i):
#         print(comb)


# str = "azycbzzzz"
#
# # a=z z=b ,y=a b=y
#
# # d={'a':'z','z':'b','y':'a','b':'y'}
# # s=''
# #
# # for ch in str:
# #     s=s+d[ch]
# #
# #
# # print(s)
#
# s=str.replace('z','d')
# print(s)


#
# text ="Good Morning , My Name is Indrajeet"
# l = int(len(text)/2)
# s= text[:l][::-1]
#
#
# rev=s+text[l:]
# print(rev)
#
# # for ch in text[:l]:
l=[]

for _ in range(int(input("Enter the number of student:"))):
    name = input("Enter the names")
    score = float(input("Enter the scores"))
    l.append([name,score])



print(l)