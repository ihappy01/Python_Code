s = "My name is Indrajeet"

## Reverse string without slicing
# rev=''
# for ch in s:
#     rev = ch + rev
#
# print(rev)

words = s.split()
# nw=[]
# for word in words:
#     nw.append(word[::-1])
#
# print((' ').join(nw))

nw= []
for word in words:
    rev=''
    for ch in word:
        rev=ch + rev
    nw.append(rev)

print((' ').join(nw))



