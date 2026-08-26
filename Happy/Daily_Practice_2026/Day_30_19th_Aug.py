# Input-running  Output-1r1u2n1i1n1g

s = 'runnninggg'
d= {}

for ch in s:
    if ch in d:
        d[ch]=d[ch]+1
    else:
        d[ch]=1

print(d)

count = 1
r=''
for i in range (len(s)-1):
    if s[i] == s[i+1]:
        count += 1
    else:
        r=r+str(count)+s[i]
        count = 1

r=r+str(count)+s[len(s)-1]

print(r)

