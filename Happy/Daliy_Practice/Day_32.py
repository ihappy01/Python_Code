# Find that sum of 2 element in the list is equal to particular value
# l = [2,3,5,6,7,1]
# target = 8
# length = len(l)
# comb_l = []

# for i in range(length):
#     for j in range(i+1,length):
#         if l[i]+l[j]==target:
#             comb_l.append((l[i],l[j]))
#
#
# print(comb_l)

# List operation practice
# l = [2,3,5,6,7,1]
# l.insert(3,8)
# print(l)
# l.remove(7)
# print(l)
# l.pop()
# print(l)
# l.pop(0)
# print(l)


# generator

# def num():
#     for i in range(10):
#         yield i
#
# gen_obj = num()
# print(next(gen_obj))
# print(next(gen_obj))
# print(next(gen_obj))
#
# l=[7,5,36,7]
#
# it_on=iter(l)
# print(next(it_on))
# print(next(it_on))


# Find the occurence of each charcter and also the character which is repeated most
# word = "mississippi"
# d={}
#
# # for ch in word:
# #     if ch in d:
# #         d[ch]=d[ch]+1
# #     else:
# #         d[ch]=1
#
# for ch in word:
#     d[ch]=d.get(ch,0)+1
#
# print(d)
# print(max(d,key=d.get))


# prime

def prime(num):
    if num==1:
        print("Not prime")
    else:
        for i in range(2,num):
            if num%i==0:
                print("Not Prime")
                break
        else:
            print("Prime Num")


prime(4)