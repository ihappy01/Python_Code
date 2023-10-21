import pytest


@pytest.mark.smoke
def test_sample_one():
    print("Inside test sample one")

@pytest.mark.regression
def test_sample_two():
    print("Inside test sample two")

@pytest.mark.regression
def test_sample_three():
    print("Inside test sample three")

@pytest.mark.sanity
def test_sample_four():
    print("Inside test sample four")

@pytest.mark.smoke
def test_sample_five():
    print("Inside test sample five")

@pytest.mark.sanity
def test_sample_six():
    print("Inside test sample six")