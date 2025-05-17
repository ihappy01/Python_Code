
def greeting(fx):
    def mfx(*args,**kwargs):
        print("Good Morning all!!")
        fx(*args,*kwargs)
        print("Thanks for using function")
    return mfx


@greeting
def hello():
    print("Hello, World")

@greeting
def add(a,b):
    print(f"The addition of the numbers are {a+b}")


hello()
add(6,7)