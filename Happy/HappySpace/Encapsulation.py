
class Finance:
    def __init__(self):
        self.__revenue = 100000   # Private data  using __
        self._no_of_sales =122    # Protected data using _

    def display(self):
        print(f"Revenue is {self.__revenue} and the sales is {self._no_of_sales}")
        self.__revenue = 200000
        print(f"Revenue is {self.__revenue} and the sales is {self._no_of_sales}")



f1 = Finance()
# f1.display()
f1._no_of_sales=130
print(f1.__dict__)
# print(f1.__revenue)   # throws AttributeError after declaring value as private


# class HR:
#     def __init__(self):
#         self.no_of_employee = 32
#         f1.__revenue = 1    # No modification allowed after declaring private, instead new variable is created
#
#
# h1 =HR()
# print(f1.__dict__)
