# Code to Reverse each word in the sentence
text = "Hello World"

words=text.split(" ")
l=[]

for word in words:
    l.append(word[::-1])

print(' '.join(l))


