# from  itertools import combinations
# l = [1,2,3]
#
# # Generate all possible combination
#
# for i in range(1,len(l)+1):
#     comb = combinations(l,i)
#     for com in comb:
#         print(com)



# Remove duplicate for list:
# l = [1,1,2,2,3,3,4,4,67,8,9,0,0,0]
# l_unique= []
#
# for i in l:
#     if i not in l_unique:
#         l_unique.append(i)
#
# print(l_unique)

#Print reverse list without using slicing

text =" Hello good Morning"

rev_text = ''

for ch in text:
    rev_text = ch + rev_text

print(rev_text)



