

# s = input("The message:")
#
# print(s)
# l=[]
# for ch in s:
#     if ch not in l:
#      print(ch, "Occurred",s.count(ch), 'times')
#      l.append(ch)


s ="Hello Good Morning"

d={}

for ch in s:
    d[ch]=d.get(ch,0) + 1

print(d)
for key,value in sorted(d.items()):
    print(f"{key} occured {value} times")