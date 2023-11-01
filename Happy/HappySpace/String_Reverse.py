text = "Hello World, Good Morning"

# method 1: using slicing
# print(text[::-1])

#Method 2 : using for loop
# s=''
# for ch in text:
#     s=ch+s
# print(s)

#Method 3: using while loop
ch=list(text)
left,right = 0, len(ch)-1

while left<right:
    ch[left],ch[right]=ch[right],ch[left]
    left=left+1
    right=right-1

print("".join(ch))


# To reverse each word in the 