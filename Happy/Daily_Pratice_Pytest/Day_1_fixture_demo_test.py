
import pytest


@pytest.fixture()
def setup_teardown():
    print("\nOpen the browser")
    yield
    print("\nClose the browser")

# The fixture to check if the test is passed or failed when one of the
@pytest.fixture()
def a_fix():
    print("Setup for fixture b")
    yield
    # assert False
    print("Teardown for fixture B")


def test_func(setup_teardown,a_fix):
    print("Login is performed")
