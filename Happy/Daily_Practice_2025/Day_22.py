from pickletools import long1

#
# Input: d = { }
# 	     l = [1,2,3,4]
# 	    n= 10
# output:  d = {1: 10, 2:10,, 3:10, 4:10}


d = { }
l = [1,2,3,4]
n =10

for i in l:
    d[i]=n

print(d)


str = "azyb"

# a=z z=b ,y=a b=y
d ={ 'a':'z', 'z':'b' ,'y':'a' ,'b':'y'}
s=''

for ch in str:
    # if ch in d:
    #     s=s+ d.get(ch,ch)
        s=s+ d[ch]

print(s)

# def custom_replace(input_str):
#     mapping = {
#         'a': 'z',
#         'z': 'b',
#         'y': 'a',
#         'b': 'y'
#     }
#     d = {'a': 'z', 'z': 'b', 'y': 'a', 'b': 'y'}
#     result = ''
#     s=''
#     for char in input_str:
#         # result += d.get(char, char)  # if char not in mapping, keep it unchanged
#         s += d.get(char, char)  # if char not in mapping, keep it unchanged
#
#     return s
#
#
# # Input
# input_str = "azyb"
# output = custom_replace(input_str)
# print("Output:", output)


l = [1,1,2,2,3,3,4,4,67,8,9,0,0,0]

l1 =[]

for i in l:
    if i not in l1:
        l1.append(i)

# [l1.append(i) for i in l if i not in l]
# print(l1)


print(list(enumerate(l)))