
#
s = "aabbccccddd"
# output = a2b2c4,d3
count =1
st=""

for i in range(len(s)-1):
    if s[i]==s[i+1]:
        count=count+1
    else:
        st=st+s[i]+str(count)
        count=1

st = st+s[i]+str(count)



print(st)