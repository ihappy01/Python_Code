import pytest


@pytest.mark.usefixtures("login_data")
class TestExample2:

    def editprofile(self, login_data):
        print(login_data)
