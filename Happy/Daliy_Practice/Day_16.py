# text="Hello Good Morning"
# s=" "
# # for ch in text:
# #     s=ch+s
# #
# # print("The reverse string is: ",s)
#
# # l=text.split(" ")
# # rev_word=l[::-1]
# # print((" ").join(rev_word))

# l=[8,4,88,3,99,101,6,25,7,4,102]
# max=l[0]
# sec_max=l[0]
# length=len(l)
# # for i in l:
# #     if i>max:
# #         sec_max=max
# #         max=i
# #     elif i>sec_max and i!=max:
# #         sec_max=i
# #
# # print(sec_max)
#
# for i in range(length):
#     for j in range(length-i-1):
#         if l[j]>l[j+1]:
#             l[j],l[j+1]=l[j+1],l[j]
#
# print(l)

#Print unique value
# l=[8,4,88,3,99,101,6,25,7,4,102,3,7,7]
# # l1=[]
# # for i in l:
# #     if i not in l1:
# #         l1.append(i)
# #
# # l1.sort()
# # print(l1)
#
# d={}
#
# for i in l:
#     d[i]=d.get(i,0)+1
#
# # print(d)
# # print(max(d,key=d.get))
# print(list(sorted(d.keys())))


# class A:
#     def method(self):
#         print("Class A Method")
#
#
#
# class B(A):
#     def method(self):
#         super().method()
#         print("Class B Method")
#
#
# ob=B()
# ob.method()
# # ob1= A()
# # ob1.method()
# # super(B,ob).method()
# ================================

# def even_or_odd(num):
#     result = ['Even','Odd']
#     print(f"The number {num} is {result[num%2]}")

# even_or_odd(7)


# =================

def even_or_odd(num):
    results = ['Even','Odd']
    return results[num%2]

for i in range(1,20):
    result = even_or_odd(i)
    print(f"{i} is {result}")