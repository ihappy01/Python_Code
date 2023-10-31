
def reverse_substring(s,size):
    result=""
    i=0
    length=len(s)

    while i<length:
        # if i<length:
            result=result+s[i:i+size][::-1]
            i=i+size

        # else:
        #     result=result+s[i:][::-1]
        #
        #     break

    return result


text= "Hello World"
size=2

print(reverse_substring(text,size))
