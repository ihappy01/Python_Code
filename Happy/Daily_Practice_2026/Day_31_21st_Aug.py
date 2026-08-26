
s = '***'

print(any(ch.isalnum()for ch in s))

# res = False
# for i in s:
#     if i.isalpha():
#         res = True
#         break
# print(res)

res = False
print(bool(res for i in s if i.isalpha()))