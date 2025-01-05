
"""
str= "Happy"
rev=''


for ch in str:
    rev=ch+rev

print("The word after reverse is:",rev)
print("The word after reverse is:",str[::-1])
"""

s = "My name is Happy"

# r= s.split(' ')
# print((r)
#
# print("The sentence after reversing is:",' '.join(r[::-1]))

l=s.split(' ')
rev=[]

for word in l:
    rev.append(word[::-1])

print("The each word of the sentence is reversed:")
print(" ".join(rev))

