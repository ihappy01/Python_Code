

s = "aaaasssdddjjjfffioopptsss"
d={}
for ch in s:
    d[ch]=d.get(ch,0)+1

print(d)
count=1
# print(f"{max(d,key=d.get)} is repeated highest time in given string")
for key,value in d.items():
    if value == 1:
        count = count + 1
        # print(f"{key} is the first element which is not repeated")
        continue
        if count==2:
            print(key)
