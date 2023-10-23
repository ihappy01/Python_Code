# l=[45,56,73,99,13,33,37]
# max=l[0]
# sec_max=l[0]
#
# for i in l:
#     if i>max:
#         sec_max=max
#         max=i
#     elif i>sec_max and i!=max:
#         sec_max=i
#
# print(sec_max)


def reverse_substring(s,size):
    i=0
    result=""
    length= len(s)

    while i<length:
        if i<length:
            result = result+s[i:i+size][::-1]
            i=i+size
        else:
            result = result + s[::-1]

    return result

text = "Hello Wolrd"
size=2

print(reverse_substring(text,size))


