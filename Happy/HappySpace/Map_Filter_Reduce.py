
l = [9,2,5,7,6,4]

# def cube(i):
#     return i*i*i

# l1 = list(map(cube,l))
l1 = list(map(lambda x: x*x*x,l))
print(l1)

#=============================
#Filter
def filter_function(x):
    return x>4


l2 = list(filter(filter_function,l))
print(l2)

l3 = list(filter(lambda x: x%2==0,l))
print(l3)

#=========================================
#Reduce
from functools import reduce
num = [1,2,3,4,5]

# calculate the sum of the number using the reduce function
def my_sum(x,y):
    return x+y


sum = reduce(my_sum,num)
# sum = reduce(lambda x,y:x+y,num)
print(sum)


# ================================================
# Write a program to find even numbers present in a list
l = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

new_l =  list(filter(lambda x:x%2==0,l))
print("The even m=numbers present the list are ",new_l)