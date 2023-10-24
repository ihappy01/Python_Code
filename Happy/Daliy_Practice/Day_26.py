# from functools import reduce
#
# l = [1, 1, 2, 2, 3, 3, 4, 4,4,4, 67, 8, 9, 0, 0, 0]
#
# # l1=[]
# #
# # for i in l:
# #     if i not in l1:
# #         l1.append(i)
# #
# # print(l1)
#
# d={}
#
# for i in l:
#     if i in d:
#         d[i]=d[i]+1
#     else:
#         d[i]=1
#
# print(d)
#
#
# # for i in l:
# #     d[i]=d.get(i,0)+1
#
# # print("The unique values of given list are:",sorted(list(d.keys())))
# # new_l=(list(d.keys()))
# # print(d)
# # print(max(d,key=d.get))
# # print(new_l)
# # length= len(new_l)
# # print(new_l)
# #
# # for i in range(length-1):
# #     for j in range(length-i-1):
# #         if new_l[j]>new_l[j+1]:
# #             new_l[j],new_l[j+1]=new_l[j+1],new_l[j]
# #
# # print(new_l)
#
#
# #Lambda funtion to print even num
# # l = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
# #
# # # l1= [x for x in l if x%2==0]
# # # l1 = list(filter(lambda x:x%2==0,l))
# # l1 = list(filter(lambda x:x>4,l))
# # print(l1)
#
# # l = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
# #
# # new_l= reduce(lambda x,y:x+y,l)
# # print(new_l)
#
#
# #
# # def num():
# #     for i in range(10):
# #         yield i
# #
# #
# # gen_ob=num()
# # print(next(gen_ob))
# # print(next(gen_ob))
# # print(next(gen_ob))
#
# #
# # l=[1,2,3]
# # l1=[4,5,6]
# # new_list=[]
# #
# # for i in (l,l1):
# #     for j in i:
# #         new_list.append(j)
# #
# # print(new_list)
#
# # # d1 ={"Name":"Dalvir","Location":"Bengaluru","Salary":98765}
# # # d2 = {"Empl_No":4,"Designation":"Manager"}


# import re
#
# text='''Chloroform, or trichloromethane (often abbreviated as TCM), is an organic compound with the formula
# CHCl3 and a common solvent. It is a 10.433.536 very volatile, colorless, strong-smelling,
# dense liquid produced on a large scale as a precursor to PTFE and refrigerants[10] and
# is a trihalomethane that serves as a powerful anesthetic, euphoriant, anxiolytic, and
# sedative when inhaled or ingested. Chloroform was used as an anesthetic between the 19th century
# and the first half of the 20th century  10.123.456'''
#
# # match=re.findall(r'\w+',text)
# # print(len(match))
#
# matches = re.finditer(r'\d{2}.\d{3}.\d{3}',text)
#
# for match in matches:
#     print(match)



# def prime(num):
#     if num==1:
#         print("not prime")
#     else:
#         for i in range(2,num):
#             if num%i==0:
#                 print("Not Prime")
#                 break
#         else:
#             print("Prime Number")
#
#
# prime(3)


# def fib(num):
#     n1=0
#     n2=1
#     next_num=0
#     for i in range(num):
#         print(next_num)
#         n1=n2
#         n2=next_num
#         next_num=n1+n2
#     # return next_num

#
# pos=fib(7)
# print("The fib num at given position is ",pos)


# l=[1,4,2,7,3,8]
# length=len(l)
# for i in range(length-1):
#     for j in range(length)


for x in range(1,11):
    print(f'{x:02d} {x*x:03d} {x*x*x:04d}')

