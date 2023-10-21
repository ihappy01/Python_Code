# Any pytest file should start with test_ or end with _test
# pytest method names should start with test
# Any code should be wrapped in method only
# Method name should have sense
# -k stands for method names execution, -s logs in output -v stands for more metadata
# you can run specific file with py.test <filename>
# you can mark (tag) tests @pytest.mark.smoke and then run with -m
# you can skip tests with @pytest.mark.skip
# @pytest.mark.xfail
# fixture are used as setup and tear down method for test cases - conftest file to generalize
# fixture and make it available to all test cases (fixture name into parameters of method)
# data driven and parameterization can be done with the return statements in the tuple format
# when you define fixture scope to class only , it will run once before class is initiated and at the end
# Use --html=report.html to create report from command line

import pytest


@pytest.mark.smoke
def test_firstProgram(setup):
    print("Hello")


@pytest.mark.xfail
def test_secondGreetCreditCard():
    print("Good Morning")


def test_crossBrowser(crossBrowser):
    print(crossBrowser[1])


