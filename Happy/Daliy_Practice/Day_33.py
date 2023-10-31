
# def num():
#     for i in range(10):
#         yield i
#
# gen_ob=num()
# print(next(gen_ob))
# print(next(gen_ob))
# print(next(gen_ob))


# text = "I am python"



#--------------------------------
# def reverse_string_with_space(s):
#     ch = list(s)
#     print(ch)
#
#     left,right = 0, len(ch)-1
#
#     while left<right:
#         #skip space while moving left pointer
#         while left<right and ch[left]==' ':
#             left=left+1
#         # skip space while moving left pointer
#         while left<right and ch[right]==' ':
#             right=right-1
#
#         #swap character at left and right position
#         ch[left],ch[right] = ch[right],ch[left]
#
#         #Move the pointer
#         left=left+1
#         right=right-1
#
#     rev_s = ''.join(ch)
#
#     return rev_s
#
#
# text = "I am python"
# output = reverse_string_with_space(text)
# print(output)


# Reverse string using while loop
# text = "I am python"
#
# ch=list(text)
# left,right=0,len(ch)-1
#
# while left<right:
#     ch[left],ch[right] = ch[right],ch[left]
#
#     left=left+1
#     right=right-1
#
#
# rev="".join(ch)
# print(rev)
#
# text = "I am python"
#
# def reverse_using_length(s,n):
#     l=len(s)
#     i=0
#     result=""
#
#     while i<l:
#         if i>n:
#             result=result+s[0:n][::-1]
#             i=i+n
#         else:
#             result=result+s[i:0][::-1]
#             break
#
#     return result
#
#
# print(reverse_using_length(text,4))


# l=12
i=0

while i<12:
    if i<12:
     print(i)
     i=i+1
    else:
        print(12)
        break