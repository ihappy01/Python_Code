class A:
    def method(self):
        print("Class A Method")



class B(A):
    def method(self):
        # super().method()
        print("Class B Method")


ob=B()
ob.method()
# ob1= A()
# ob1.method()
super(B,ob).method()
