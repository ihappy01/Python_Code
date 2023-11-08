# text=  "Hello Good Morning, Indrajeet"
# d={}
#
# for ch in text:
#     if ch in d:
#         d[ch]=d[ch]+1
#     else:
#         d[ch]=1
#
# print(d)
# print(max(d,key=d.get))


# To store class object as list

class Movie(object):
    def __init__(self,title,duration,hero):
        self.title = title
        self.duration = duration
        self.hero = hero


    def display(self):
        print(f"Title is: {self.title}\nDuration is {self.duration}\nHero is {self.hero}\n=======================")


movie_list=[]

while True:
    title=input("Enter movie title:")
    duration=input("Enter movie duration:")
    hero=input("Enter movie hero:")

    ob=Movie(title,duration,hero)
    movie_list.append(ob)
    print("Movie details are added")

    ans =input("Do you want to add another movie detail(y/n):")
    if ans!='y':
        break

for ob in movie_list:
    ob.display()


