# 5. Write a program to combine 2 list as a dictionary.
import textwrap

l= ['a','b','c']
l1 = [1,2,3]
d={}

result = dict(zip(l,l1))
print(result)

# for i in range(len(l)):
#     d = zip(l,l1)


# print(dict(d))
# print(list(d))
# print(tuple(d))

letters = ['A', 'B', 'C']
numbers = [1, 2, 3, 4, 5] # '4' and '5' will be discarded

# print(list(zip(letters, numbers)))
print(list(zip(numbers, letters)))


s='ABCDEFGHIJKLIMNOQRSTUVWXYZ'

r= textwrap.fill(s,4)
print(r)
# print(textwrap.fill(s,4))
