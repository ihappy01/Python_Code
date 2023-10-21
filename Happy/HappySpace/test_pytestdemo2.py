import pytest

@pytest.fixture()
def setup():
    print("\nOnce before every method")
    yield
    print("\nOnce after every method")


def testmethod1(setup):
    print("This is method-1")

def testmethod2(setup):
    print("This is method-2")
