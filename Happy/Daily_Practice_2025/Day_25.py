from socks import method


class A:
    def method1(self):
        print("A")


class B(A):
    def method1(self):
        print("B")



ob = A()
a= ob.method1()
# print(ob.method1())

print(hasattr(ob,"method1") and callable(ob))