s = 'Hello my name is indrajeet'

words=s.split(' ')
r=''
for word in words:
    r= r + ' ' +word[::-1]


print(r)



l=[]

for word in words:
    l.append(word[::-1])

print((' ').join(l))


rs = ''

for word in words:
    rw =''
    for ch in word:
        rw = ch+rw
    print(rw)
    rs=rs + rw+ ' '

print(rs)
