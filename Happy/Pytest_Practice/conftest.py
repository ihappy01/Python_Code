import pytest


@pytest.fixture
def setup_and_teardown():
    print("Launch the browser")
    print("Open application URL in browser")
    yield
    print("Logout from the application")
    print("Close the browser")

    