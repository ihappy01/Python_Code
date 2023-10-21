import pytest


@pytest.fixture(scope="class")
def setup():
    print("I will be executing first Setup from fixture")
    yield
    print("I will be executed last Teardown from fixture")


@pytest.fixture()
def login_data():
    print("User profile data is being created")
    return ["Indrajeet", "Happy", "indrajeet_happy@gmail.com"]
