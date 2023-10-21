str = "qwertyuiopasdfghjklzxcvbnm"

l=len(str)
for i in str[2:l:3]:
    print(i)


"""
Read the excel and print it in key value
"""
l= ['a','b','c']
l1 = [1,2,3]
dic1={}

length= len(l)

for i in range(length):
    dic1=dict(zip(l,l1))

print(dic1)