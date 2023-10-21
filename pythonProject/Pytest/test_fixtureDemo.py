import pytest


# def test_fixture_demo(setup):
#     print("I will execute steps in fixture demo methods")

@pytest.mark.usefixtures("setup")
class Login:

    def test_fixture_1(self):
        print("This is test fixture 1 ")

    def test_fixture_2(self):
        print("This is test fixture 2")
    #
    # @pytest.fixture(login_data)    `
    # def test_login_page_use_fixture_data(self,login_data):


