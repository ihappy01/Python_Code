import pytest


class Test:



    @pytest.fixture()
    def myfixture(self):
        print("\nmy fixture is called")
        return("Hello World")

    @pytest.fixture()
    def myfixture1(self,myfixture):
        return myfixture + ",Good Morning"

    def test_method1(self,myfixture1):
        print("Method-1 is called")
        print(myfixture1)

    def test_method2(self,myfixture):
        print("\nMethod-2 is called")

