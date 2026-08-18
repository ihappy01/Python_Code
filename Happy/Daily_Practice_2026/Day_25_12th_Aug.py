

s = "ABCDCDC"
ss = "CDC"

#Working
sl = len(s)
subl = len(ss)
count =0


for i in range((sl-subl+1)):
    if s[i:i+subl] == ss:
        count = count+1

print(count)

# Working
c=0
for i in range(len(s)):
  if s.find(ss,i) == i:
      print(i)
      c += 1
print(c)