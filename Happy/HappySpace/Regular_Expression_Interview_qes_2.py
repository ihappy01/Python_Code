#To find special character without using isalpha
import re
s= "12345^dfghj&oi@78"

# match=re.findall(r'[^a-zA-Z0-9]',s)
match=re.findall(r'\W+',s)
print(match)