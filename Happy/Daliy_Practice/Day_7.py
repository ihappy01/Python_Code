# decorator

def greet(fx):
    print("Hello , Good Morning")
    def mfx(*args,**kwargs):

        fx(*args,**kwargs)
        print("Hello, Good Evening")
    return mfx



@greet
def add(a,b):
    print("Add function")
    print(a+b)

add(7,9)

