import re

text_to_search = '''
abcdefghijklmnopqrstuvwxyz
ABCDEFGHIJKLNMOPQRSTUVWXYZ
1234567890

Ha HaHa

MetaCharacters (Need to be escaped):
. ^ $ * + ? { } [ ] \ | ( )

coreyms.com

321-555-4321
123.555.1234
800.555.1234
900-555-4321

Mr. Schafer
Mr Smith
Ms Davis
Mrs. Robinson
Mr. T

cat
mat
pat
bat
'''
sentence ='Start a sentence and then end bring it to an end'

emails = '''
CoreyMSchafer@gmail.com
corey.schafer@university.edu
core-321-schafer@my-work.net
'''

urls = '''
https://www.google.com
https://coreyms.com
https://youtube.com
https://www.nasa.gov
'''
# match = re.search(r'\d{3}-\d{3}-\d{3}',text_to_search,re.IGNORECASE)
# print(match)
# print(match.group())
# print(type(match))

# pattern = re.compile(r'\d{3}-\d{3}-\d{3}')
# matches = pattern.findall(text_to_search)
#
# print(matches)
# print(type(matches))

# pattern = re.compile(r'\BHa')
#
# matches = pattern.findall(text_to_search)
#
# print(matches)


# text = "On 2023-09-07, the conference will begin. TRhe event will end on 2023-09-19"
#
# data_pattern = r'\d{4}-\d{2}-\d{2}'
#
# dates = re.findall(data_pattern,text)
#
# print(dates)

#
# data = 'abaababa'
#
# pattern = re.compile(r'ab')
#
# matches = re.finditer(pattern,data)
# # matches = pattern.finditer(data)
#
# print(matches)
#
#
# for match in matches:
#     # print("===========")
#     # print(match.group())
#     print(match.start())
#     print(match.end())
#     print(data[match.start():match.end()])


# data= "I saw Dog running behind cat and cat climbed but dog couldn't"
#
# pattern = re.compile(r'dog|cat',re.IGNORECASE)
#
# print(pattern.findall(data))

data = "The price is $100"

patter = r'[\d]'

match = re.findall(patter,data)
print(match)
