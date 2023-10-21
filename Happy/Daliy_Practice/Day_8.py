# Find Occurrence of each character
# text ="Hello World"
# l=[]
# d={}
# for ch in text:
#     if ch not in l:
#      l.append(ch)
#      count=text.count(ch)
#      print(f"The {ch} is having {count} occurrence")

# Second Method
# for ch in text:
#     d[ch]=d.get(ch,0)+1
#
#
# print(d)
#
# for key,value in d.items():
#     print(f"{key} is having {value} occurrence")
# =============================================================
import re

text='''11/18/2022 ERROR wow message such ERROR ERROR long
11/18/2022 INFO wow message such ERROR long
11/19/2022 WARNING wow message such ERROR long
11/19/2022 ERROR wow message such ERROR long'''

# lines = text.split('\n')
keyword={}

# for line in lines:
#     matche =re.search(r'\d{2}/\d{2}/\d{4}\s(\w+)',line)
#     # print(matche.group(1))
#     if matche:
#         index=matche.group(1)
#         keyword[index]=keyword.get(index,0)+1



# print(keyword)

with open('../HappySpace/log_file.txt', 'r') as f:
    lines=f.readlines()
    for line in lines:
        matche = re.search(r'\d{2}/\d{2}/\d{4}\s(\w+)', line)
        # print(matche.group(1))
        if matche:
            index = matche.group(1)
            keyword[index] = keyword.get(index, 0) + 1

print(keyword)