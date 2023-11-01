# Code to Reverse each word in the sentence
# text = "Hello World"
#
# words=text.split(" ")
# l=[]
#
# for word in words:
#     l.append(word[::-1])
#
# print(' '.join(l))


# reverse substring
# text = "Hello World"
# l=len(text)
# i=0
# size=5
#
# result= ""
#
# while i<l:
#     result=result+text[i:i+size][::-1]
#     i=i+size

# print(result)

# sum of list element to target
# a=[3,5,2,7,1,8,9]
# target=9
# l = len(a)
# b=[]
#
# for i in range(l):
#     for j in range(i+1,l):
#         if a[i]+a[j]==target:
#             b.append((a[i],a[j]))
# print(b)

# Add 2 dictionary
# d1 ={"Name":"Dalvir","Location":"Bengaluru","Salary":98765}
# d2 = {"Empl_No":4,"Designation":"Manager"}
# md ={}
# # for d in (d1,d2):
# #     for key,value in d.items():
# #         md[key]=value
#
# for d in (d1,d2):
#     for key in d:
#         md[key]=d[key]
# print(md)


# For else loop working

for i in range(5):
    print(i)
    if i==3:
        break
else:
    print("Sorry no i")











