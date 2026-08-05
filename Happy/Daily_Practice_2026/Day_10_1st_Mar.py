

s = "The America and Isreil has attacked Iran"

s1= s.split(' ')
str1=''
for word in s1:
    str1=str1 + ' ' + word[::-1]

print(str1)