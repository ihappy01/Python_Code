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


# pattern = re.compile(r'abc')
# pattern = re.compile(r'\bHa')
# pattern = re.compile(r'coreyms\.com')
# pattern = re.compile(r'end$')
# pattern = re.compile(r'\d{3}-\d{3}-\d{3}')
# pattern = re.compile(r'\d{3}')
# pattern = re.compile(r'[89]00.\d{3}.\d{3}')
# pattern = re.compile(r'M[a-z]*.\s[A-Z]\w*')
# pattern = re.compile(r'(Mr|Ms|Mrs).?\s[A-Z]\w*')
# pattern = re.compile(r'[a-zA-Z0-9.-]+@[A-Za-z-]+\.(com|edu|net)')



pattern = re.compile(r'https?://(www\.)?([a-z]+)(\.[a-z]+)')
subbed_urls = pattern.sub(r'\2\3',urls)
print(subbed_urls)






# matches = pattern.finditer(text_to_search)
# matches = pattern.finditer(sentence)
# matches = pattern.finditer(emails)


matches = pattern.finditer(urls)

for match in  matches:
    print(match.group(3))







# Matching inside a file
# with open('data.txt','r') as f:
#     text =f.read()
#
#
# pattern_1=re.compile(r'\d{3}.\d{3}.\d{3}')
#
# matches = pattern_1.finditer(text)
#
# for match in matches:
#     print(match)