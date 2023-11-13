text = "Hello Good Morning, My name is Indrajeet"
# s=text.split(' ')
# l=''
# for word in s:
#    l = l+' '+ word[::-1]
#
#
# print(l)

ch=list(text)
l=len(text)
left,right= 0,l-1

while left<right:
    if ch[left]== " ":
        left= left+1

    if ch[right]==" ":
        right=right-1

    ch[left],ch[right]=ch[right],ch[left]

    left=left+1
    right=right-1


print("".join(ch))

