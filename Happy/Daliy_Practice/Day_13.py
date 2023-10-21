
# str = "azyb"
# # a=z z=b ,y=a b=y
#
# d={'a':'z','z':'b','y':'a','b':'y'}
# s=""
#
# for ch in str:
#     if ch in d:
#         s=s+d[ch]
#
# print(s)

#---------------------------------
# d = {}
# l = [1,2,3,4]
# n= 10
# #
# # for key in l:
# #     d[key]=n
# #
# # print(d)
#
# d ={key:n for key in l}
# print(d)
#----------------------------



#
#
# class ParentClass:
#
#     def parent_method(self):
#         print("This is parent method1")
#
# class ChildClass(ParentClass):
#     # def parent_method(self):
#     #     print("Indrajeet")
#     #     super().parent_method()
#
#     def child_method(self):
#         print("This is the child method")
#         super().parent_method()
#
# child_obj = ChildClass()
# child_obj.parent_method()
# child_obj.child_method()
#
#
# ======================

class Employee:
    def __init__(self,name,id):
        self.name=name
        self.id=id


class Programmer(Employee):
    def __init__(self,name,id,lang):
        super().__init__(name,id)
        self.lang=lang


p1 =Programmer("Indrajeet",43,"python")

print(p1.name,p1.lang)