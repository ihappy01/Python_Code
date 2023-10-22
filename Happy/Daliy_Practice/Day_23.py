# # d1 ={"Name":"Dalvir","Location":"Bengaluru","Salary":98765}
# # d2 = {"Empl_No":4,"Designation":"Manager"}
# #
# # # d1.update(d2)
# # # print(d1)
# # # new_d={}
# # # for d in [d1,d2]:
# # #     for key in d:
# # #         new_d[key]=d[key]
# # #
# # #
# # # print(new_d)
# #
# # # new_d={}
# # # for d in (d1,d2):
# # #     for key in d:
# # #         new_d[key]=d[key]
# # #
# # #
# # # print(new_d)
# #
# # #
# # # l=[1,4,5]
# # # l1= [2,4,5]
# # #
# # # for value in [l,l1]:
# # #  for i in value:
# # #     print(i,end=" ")
# #
# #
# # def add_extension(func):
# #     def wrapper(*args):
# #         # if len(args) != 4:
# #         #     raise ValueError("The function should be called with exactly 4 values.")
# #         result = sum(args)
# #         return result
# #     return wrapper
# #
# # @add_extension
# # def add(a, b):
# #     return a + b
# #
# # # The original 'add' function works with 2 values:
# # # result_2 = add(1, 2)
# # # print(result_2)  # Output: 3
# #
# # # The 'add' function with the 'add_extension' decorator works with 4 values:
# # result_4 = add(1, 2, 3, 4,5)
# # print(result_4)  # Output: 10
# #
# # # If you try to use the decorated 'add' function with a different number of values, it will raise an error:
# # # add(1, 2, 3)  # Raises ValueError
#
# #
# # l2=[1,2,3,4]
# # l3=[[7,8],[11,12]]
# #
# # # l2.append(l3)
# # # # l2 =[1,2,3,4,[[7,8],[11,12]]]
# # # print(l2)
# # l2.extend(l3)
# # # l2 =[1,2,3,4,[[7,8],[11,12]]]
# # print(l2)
#
#
# from itertools import combinations
#
# def find_combinations_with_sum(arr, target_sum):
#     result = []
#     for r in range(1, len(arr) + 1):
#         for combo in combinations(arr, r):
#             if sum(combo) == target_sum:
#                 result.append(combo)
#     return result
#
# l = [1, 2, 40, 3, 9, 4, 5, 3, 7]
# target = 6
#
# combinations_with_sum = find_combinations_with_sum(l, target)
#
# if combinations_with_sum:
#     print(f"Combinations with sum {target} are:")
#     for combo in combinations_with_sum:
#         print(combo)
# else:
#     print(f"No combinations found with sum {target}.")


from itertools import combinations

def find_combinations_with_sum(arr, target_sum):
    result = []
    for combo in combinations(arr, 2):
        if sum(combo) == target_sum:
            result.append(combo)
    return result

l = [1, 2, 40, 3, 9, 4, 5, 3, 7]
target = 6

combinations_with_sum = find_combinations_with_sum(l, target)

if combinations_with_sum:
    print(f"Combinations with sum {target} are:")
    for combo in combinations_with_sum:
        print(combo)
else:
    print(f"No combinations found with sum {target}.")

