
text="My name is Indrajeet"
i=0
l=len(text)
size=4
s=''

while i<l:
    s=s+text[i:i+size][::-1]
    i=i+size


print(s)