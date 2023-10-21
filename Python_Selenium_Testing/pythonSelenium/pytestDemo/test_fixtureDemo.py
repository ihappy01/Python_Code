import pytest


@pytest.mark.usefixtures("setup")
class TestExample:

    def test_fixtureDemo(self):
        print("I am executing steps in fixtureDemo method")

    def test_fixtureDemo1(self):
        print("I am executing steps in fixtureDemo1 method")

    def test_fixtureDemo2(self):
        print("I am executing steps in fixtureDemo2 method")

    def test_fixtureDemo3(self):
        print("I am executing steps in fixtureDemo3 method")