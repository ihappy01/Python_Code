def reverse_substring(s,size):
    i=0
    result =""

    while i<len(s):
        if i+size <= len(s):
            result = result + s[i:i+size][::-1]
            i= i+size
        else:
            result = result + s[i:][::-1]
            break

    return result


text = "Hello World"
size =3


rev_str =reverse_substring(text,size)
print(rev_str)

