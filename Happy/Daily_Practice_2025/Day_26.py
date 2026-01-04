# from pycparser.ply.lex import NullLogger
#
# s = "Indrajeet"
#
# # rs = ""
# # for ch in s:
# #     rs= ch + rs
#
# rs=""
# index =len(s)-1
#
# while index >= 0:
#     rs = rs + s[index]
#     index = index -1
#
# print(rs)


class Person:
    def __init__(self,**kwargs):
        # self.name = kwargs.get("name","Indrajeet")
        # self.age = kwargs.get("age",0)
        self.name = None
        self.age = 1

    def display(self):
        print(f"Name: {self.name}, Age: {self.age}")


# Create objects
p1 = Person(name="Alice", age=25)
p2 = Person(name="Bob", age=30)
p3 = Person(name="Charlie")

# Store objects in a list
people_list = [p1, p2, p3]

# Access and use objects from the list
for person in people_list:
    person.display()
