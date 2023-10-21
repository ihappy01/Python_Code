import pytest


@pytest.fixture(scope="class")
def setup():
    print("I will be executing first")
    yield
    print("I will be executed last")


@pytest.fixture()
def dataLoad():
    print("User profile data is being created")
    return ["Indrajeet", "Happy", "ihappy@gmail.com"]


@pytest.fixture(params=[("chrome","Indrajeet","Happy"), ("Firefox","Happy"), ("IE","SS")])
def crossBrowser(request):
    return request.param
