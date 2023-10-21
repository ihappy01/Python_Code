import pytest


@pytest.fixture(scope='module')
def myfixture():
    print("\nMyfixture from contest called")