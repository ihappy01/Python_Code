

text = "Hello Good Morning, My name is Indrajeet"
size=4
s=''
l=len(text)
i=0

while i<l:
    s=s+text[i:i+size][::-1]
    i=i+size

print(s)
