# def reverse_substring(s,size):
#       result=""
#       i=0
#       length = len(s)
#       while i<length:
#           if i<length:
#               result=result + s[i:i+size][::-1]
#               i=i+size
#           else:
#               result=result+s[i:][::-1]
#               break
#
#       return result
#
#
# text="Hello World"
# # size=4
# print(reverse_substring(text,3))

# ==================Not working
# def extend_additio n(*args):
#     def mfx(fx):
#         return fx(*args)
#     return mfx
#
#
# @extend_addition(7,8)
# def add(a,b):
#     return a+b
#
# add(8,7)

# ===============

# d1 ={"Name":"Dalvir","Location":"Bengaluru","Salary":98765}
# d2 = {"Empl_No":4,"Designation":"Manager"}
# n={}
#
# # d1.update(d2)
# # print(d1)
# for d in (d1,d2):
#     for key in d:
#         n[key]=d[key]

# print(n)


# d=dict([{1,"one"},[2,"two"],(3,"three")])
# print(d)

# d={x:x+5 for x in range(1,5)}
# print(d)

# for i,v in enumerate(["Hello","World","Good","Evening"]):
#     print(i, v)

l=[3,5,6,3]
l1 = ["hi","are","to","you"]

for key,value in zip(l,l1):
    print(f"{key} coded as {value}")