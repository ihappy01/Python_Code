
text = "My23namerr45is"
# text = "My name is"
ch=list(text)
l=len(text)
left = 0
right = l-1

text.isdigit()

while left<right:
    # if ch[left]==' ':
    if ch[left].isdigit()==True:
        # print(ch[left].isdigit())
        left=left+1

    # if ch[right]==' ':
    if ch[right].isdigit()==True:
        right=right-1

    ch[left],ch[right]= ch[right],ch[left]

    left=left+1
    right=right-1

print("".join(ch))

# for char in ch:

# text = "My23name45is"
#
# for ch in text:
#     if ch.isdigit()==True:
#         print(ch)

