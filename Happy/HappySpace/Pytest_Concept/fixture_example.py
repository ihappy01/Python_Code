import pytest

@pytest.fixture()
def setup():
    print("Before running test case")
    yield
    print("After running test case")


def test_example1(setup):
    print("Test case 1 is executed")

def test_example2(setup):
    print("Test case 2 is executed")


