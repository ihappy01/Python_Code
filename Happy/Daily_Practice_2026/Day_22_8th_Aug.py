s = "My name is Indrajeet"

# words = s.split(' ')
# l=[]
# for word in words:
#     l.append(word[::-1])
#
#
# print(" ".join(l)
#
# rev = [word[::-1] for word in s.split(' ')]
# print(rev)
# print(" ".join(rev))

s = "My name is Indrajeet"

# Reversing the order of words using a list comprehension
# words = s.split()
# reversed_words = [words[len(words) - 1 - i] for i in range(len(words))]
# result = " ".join(reversed_words)
#
# print(result)

rev = s.split()
print(rev)
print(" ".join(rev[::-1]))