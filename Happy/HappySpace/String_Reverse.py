text = "Hello World, Good Morning"

# method 1: using slicing
# print(text[::-1])

#Method 2 : using for loop
# s=''
# for ch in text:
#     s=ch+s
# print(s)

# Method 3: using while loop
# l = len(text)-1
# s=''
# while l >=0:
#     s = s + text[l]
#     l -= 1
#
# print(s)


# To reverse each word in the
# words = text.split(" ")
# l=[]
#
# for word in words:
#     l.append(word[::-1])
#
# print(" ".join(l))

# To reverse each word in the without slicing
words = text.split(" ")
nw= []
for word in words:
    rev=''
    for ch in word:
        rev=ch + rev
    nw.append(rev)

print((' ').join(nw))