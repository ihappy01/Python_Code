s = 'runninnngg'

r=''
count=1

for i in range(len(s)-1):
    if s[i] == s[i+1]:
        count += 1
    else:
        r = r+str(count)+s[i]
        count = 1

r = r+str(count)+s[len(s)-1]

print(r)

