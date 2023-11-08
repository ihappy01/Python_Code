class Movie(object):
    def __init__(self,title,runtime,hero):
        self.title = title
        self.runtime =runtime
        self.hero =hero

    def display(self):
        print(f"Title is {self.title}\nRuntime is {self.runtime}\nHero is {self.hero}")


movie_list=[]

while True:
    title=input("Enter Movie Title:")
    runtime=input("Enter Movie Runtime:")
    hero=input("Enter Movie Hero:")

    ob=Movie(title,runtime,hero)
    movie_list.append(ob)

    print("Movie Added to the list")
    ans=input("Do you want to add another movie(y/n):")
    if ans!='y':
        break

print("All Movie Information")
for ob in movie_list:
    ob.display()



