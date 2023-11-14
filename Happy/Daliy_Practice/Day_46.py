import re

# password = input("Enter Password:")
#
# pattern = r'[0-9A-Z]'
#
#
# data = re.findall(pattern,password)
# print(data)
#
# if data:
#     print("Valid Password")
# else:
#     print("Invalid Password")

# ====================
# text = "Hello, my phone . number is 123"
#
# # pattern = r'\d'
# # pattern = r'\D'
# pattern = r'\bphone\b'
# pattern = r'\AHello'
# pattern = r'123\Z'
# pattern = r'\.'
#
# result = re.finditer(pattern,text)
#
# for match in result:
#     print(match.start(),match.group())


# data  = "Hello World,i am Indrajeet"
#
# pattern = r'l.'
#
# matches = re.findall(pattern,data)
# matches = re.finditer(pattern,data)
#
# for match in matches:
#     print(match)

#
# data = "My email address are indr5ajeeAtcs09@gmail.com and gitcsindrajeet@gmail.com"
# pattern = r'\w+@\w+\.\w+'
#
# email_addresses = re.findall(pattern,data)
# print(email_addresses)



# pattern = r'\d'
# pattern = r'[^0-9]'
pattern = r'[0-9]{3}$'
text ='''Hello 10 56 World1234
my name is indrajeet 9865'''
matches= re.findall(pattern,text,re.MULTILINE)
print(matches)

if matches:
    print("Start with digit")
else:
    print("Does not start with digit")