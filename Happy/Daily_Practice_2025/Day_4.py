from DemoFramework.pages.LoginPage import LoginPage


class Person:
    name = "Shubham"
    occupation = "Student"
    networth= 10

    def info(self):
        print(f"{self.name} is a {self.occupation}")


a= Person()
a.name="Indrajeet"
a.occupation="Software Engineer"

print(a.name)
a.info()


#Program to find max in list :
l= [45,21,99,56,101,2,47]

# max_value = l[0]
#
# for i in l:
#     if i>max_value:
#         max_value=i
#
# print(f"The maximum value in the is list is {max_value}")

def max_value_list(l):
    max_val=l[0]

    for i in l:
        if i>max_val:
            max_val=i

    return max_val

l= [45,21,99,56,131,2,47]
# print(f"The maximum value in the is list is {max_value_list(l)}")
print("The maximum value in the is list is",max_value_list(l))


