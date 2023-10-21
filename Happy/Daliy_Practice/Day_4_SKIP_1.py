
#
# d = {'a':1,'b':2,'c':3}
#
# # convert dict into list or tuple
# print(list(d))
# print(tuple(d))

text = "abcdabcdefghabcdefgchdd"
d={}

for ch in text:
    if ch in d:
      d[ch]=d[ch]+1
    else:
      d[ch] =1

char=max(d,key=d.get)

print(f"The character having highest occurence is {char}  and it has {d[char]} count")
