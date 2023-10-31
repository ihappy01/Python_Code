
def reverse_string_with_space(s):
    ch = list(s)
    left,right=0, len(ch)-1

    while left<right:

        if ch[left]== " ":
         left=left+1

        if ch[right]== " ":
         right=right-1


        ch[left],ch[right]=ch[right],ch[left]

        left=left+1
        right=right-1

    rev_s= "".join(ch)

    return rev_s

# text="I am python"

text= "Hello world, Good Morning"
print(reverse_string_with_space(text))
