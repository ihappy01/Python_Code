s = "azyb"

# a=z z=b ,y=a b=y

d= {'a':'z','z':'b','y':'a','b':'y'}
r=''
print(d)
for ch in s:
    r=r+d[ch]

print(r)