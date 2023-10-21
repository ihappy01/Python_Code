import pytest

@pytest.fixture()
def setup():
    print("\nExecute once before every method")


def testmethod1(setup):
    print("This is test method-1")

def testmethod2(setup):
    print("This is test method-2")