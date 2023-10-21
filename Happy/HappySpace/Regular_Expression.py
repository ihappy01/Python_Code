# Python program for extracting dates from given text
import re
# ===============================================
# # Sample text containing dates
# text = "On 2023-09-17, the conference will begin. The event will end on 2023-09-19"
#
# # Regex pattern to match dates in the format YYYY-MM-DD
# date_pattern = r"\d{4}-\d{2}-\d{2}"
#
# #Find all the matches of the date pattern in the text
# dates = re.findall(date_pattern,text)
#
# #Print the extracted dates
# print(dates)

# ===================================================
#
# pattern = "Python"   # pattern to search
# data = "PYTHON is very powerful and python has lots of features"  # data to search in

# match = re.search(pattern,data,re.IGNORECASE)
# print(match)
# print(type(match))
#
# if match:
#     print("Found",match.group())
# else:
#     print("Not Found")

# ==================================================================================

text_to_search = '''
abcdefghijklmnopqrstuvwxyz
ABCDEFGHIJKLNMOPQRSTUVWXYZ
1234567890

Ha HaHa

MetaCharacters (Need to be escaped):
. ^ $ * + ? { } [ ] \ | ( )

coreysm.com

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


# pattern = re.compile(r'[a-zA-Z0-9.-]+@[a-zA-Z-]+\.(com|edu|net)') #email pattern
pattern = re.compile(r'https?://(www\.)?(\w+)(\.\w+)') #url pattern

subbed_urls = pattern.sub(r'\2\3',urls)
print(subbed_urls)
# pattern = re.compile(r'{a-z}10.[com]')

matches = pattern.finditer(urls)


for match in matches:
    print(match.group(3))

# with open('data.txt','r') as f:
#     contents = f.read()
#
#     matches=pattern.finditer(contents)
#     for match in matches:
#         print(match)

# print("\tTAB")
# print(r"\tTAB")
# print(text_to_search[1:4])
