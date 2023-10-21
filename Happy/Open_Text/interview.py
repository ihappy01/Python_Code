
str = "azyb"

# a=z z=b ,y=a b=y

str1 =""
str2 =""
l=len(str)
for i in str:
    str1 = i + str1

# for i in range l:
#     str2 = i str2

# for i in str:
#     if i== 'a':
#         str[i]='z'
#     elif i=='z':
#         str[i]='b'
#     elif i=='y':
#         str[i]='a'
#     elif i=='b':
#         str[i]='y'


print(str1)