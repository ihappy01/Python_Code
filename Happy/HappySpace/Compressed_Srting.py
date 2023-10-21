
#
text = "aabbbccccaaaaa"
count=1
output= ""
for i in range(len(text)-1):
    if text[i]==text[i+1]:
        count=count+1
    else:
        output=output+text[i]+str(count)
        count=1
output=output+text[i]+str(count)


print(output)