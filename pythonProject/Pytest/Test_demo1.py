# In Pytest file name should start with "test" or  end with "test"
# pytest method name should start with test
# Any code should be wrapped in method only
# -k stands for method name execution , -s logs in output , -v for more info
# -xfail
# fixture are used as setup and tear down methods for test cases
# - conftest file to generalize fixture and make it available to all test cases
import pytest


@pytest.mark.xfail
def test_firstprogram():
    print("Hello")


@pytest.mark.smoke
def test_SecondprogramExpressio():
    print("Hello,Worls")
