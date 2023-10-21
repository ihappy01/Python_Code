import re

# Sample text containing dates
text = "On 2023-09-17, the conference will begin. The event will end on 2023-09-19 contact on 123.555.1234"

# Regular expression pattern
# pattern = r"\d{4}-\d{2}-\d{2}"

pattern = r"\d{3}.\d{3}.\d{4}"
# pattern =
print(pattern)


# Find all matches in the given text
dates = re.findall(pattern,text)

print(dates)


# pattern = "Python"   # pattern to search
# data = "PYTHON is very powerful and python has lots of features"  # data to search in
#
# match =re.search(pattern,data,re.IGNORECASE)
# print(type(match))
# print(match.group())
