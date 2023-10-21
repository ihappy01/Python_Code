
l = [34,45,6,7,2,44,98,99,100]
lar =l[0]
sec_lar=l[0]

for i in l:
    if i>lar:
        lar=i

print(lar)

for i in l:
    if i<lar and i>sec_lar:
        sec_lar=i

print(sec_lar)
