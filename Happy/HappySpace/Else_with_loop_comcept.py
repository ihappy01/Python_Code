# The statement in the else block is executed after all iteration of the loop is completed
# The program exit loop only after else block is executed
# Execution of else means loop break nahi hua hai loop khatam hua hai
# If we break out of the loop then else block is not executed

# for i in range(5):
#     print(i)
# else:
#     print("Sorry no i")
#
#
# for j in range(5):
#     print(j)
#     if j==3:
#         break
# else:
#     print("Sorry no j")

i=0
while i<5:
    print(i)
    i=i+1
else:
    print("While loop execution completed")

# i=0
# while i<5:
#     print(i)
#     i=i+1
#     if i==4:
#         break
# else:
#     print("While loop execution completed")





