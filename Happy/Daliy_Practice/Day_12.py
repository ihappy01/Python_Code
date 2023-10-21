
# -----
# mylist = [18,-3,5,0,-1,12]
# l=[]
# for i in mylist:
#     # print(abs(i))
#     l.append(abs(i))
#
# print(l)
# l.remove(5)
# print(l)
#
# l.insert(1,"abb")
# print(l)

# -----------------------

# str = "azyb"
#
# # a=z z=b ,y=a b=y
#
# d = {'a':'z','z':'b','y':'a','b':'y'}
# s=""
#
# for ch in str:
#     if ch in d:
#         s=s+d[ch]
#
# print(s)

# ------------------------

# x3 = {"a" : 10,"b":30}   | x3 = {"a" : 10,"}
# print(x3.get("b", 20))
# print(x3["a"])


# # x={'a':10}
# x={'a':10,'b':30}
# print(x.get('b',20))


# --------------
str = "Hello World"
s=''
for ch in str:
    s=ch +s
print(s)