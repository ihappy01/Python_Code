s = "ABCDCDC"
ss = "CDC"

count = 0
sl = len(s)
sublen = len(ss)
# print (s[2:(sublen+2)])
breakpoint()
for i in range(0, sl-sublen+1):
    # print(s[i:(sublen + i)])
    if s[i:(sublen+ i)] == ss:
        print(s[i:(sublen+ i)])
        count += 1

print(count)