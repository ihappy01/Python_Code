

s = "My name is Indrajeet"

# r = ''
# for ch in s:
#     r= ch + r
#
# print(r)

words = s.split(' ')
rs = []
for word in words:
    r = ''
    for ch in word:
        r = ch + r
    rs.append(r)

print((' ').join(rs))


