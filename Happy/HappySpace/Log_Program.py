import re

# def count_keywords_in_log(log_file):
#     keyword_counts = {}
#
#     with open('log_file.txt', 'r') as file:
#         for line in file:
#             match = re.search(r'\d{2}/\d{2}/\d{4}\s+(\w+)', line)
#             if match:
#                 keyword = match.group(1).upper()
#                 keyword_counts[keyword] = keyword_counts.get(keyword, 0) + 1
#
#     return keyword_counts
#
# log_file = "your_log_file.txt"  # Replace with the path to your log file
# keyword_counts = count_keywords_in_log(log_file)
#
# print(keyword_counts)

text='''11/18/2022 ERROR wow message such ERROR ERROR long
11/18/2022 INFO wow message such ERROR long
11/19/2022 WARNING wow message such ERROR long
11/19/2022 ERROR wow message such ERROR long'''

lines = text.split('\n')
keyword_count={}

for  line in lines:
    match= re.search(r'\d{2}/\d{2}/\d{4}\s+(\w+)',line)
    # print(match.group(1))
    if match:
        keyword=match.group(1)
        print(keyword)
        keyword_count[keyword]=keyword_count.get(keyword,0)+1

print(keyword_count)

