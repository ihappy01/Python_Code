
#
# class Workload:
#     def __init__(self,duration,workload_type):
#         self.duration = duration
#         self.workload_type = workload_type
#
#     def start(self):
#         cmd =f"dd workload={self.workload_type} duration={self.duration} bs=1M"
#         print(cmd)
#
#     def display(self):
#         print(f"The {self.workload_type} is running")
#
# class Vdbench(Workload):
#     def __init__(self,duration,workload_type,profile):
#         super().__init__(duration,workload_type)
#         self.profile = profile
#
#     def start(self):
#         cmd = f"dd workload={self.workload_type} duration={self.duration} profile={self.profile} bs=1M"
#         print(cmd)
#
#
#
# wd = Workload(300,'Fio')
# wd.start()
# wd.display()
#
# vd = Vdbench(600,'vdbench','EDA')
# vd.start()
# vd.display()


class Book:
    def __init__(self,title,author):
        self.title = title
        self.author = author

class Library(Book):
    def __init__(self):
        self.books = []

    def add_book(self,book):
        self.books.append(book)

    def dispaly(self):
        for book in self.books:
            print(f'{book.title} by {book.author}')

library = Library()
library.add_book(Book("Intelligent investor","Benjamin Graham"))
library.dispaly()