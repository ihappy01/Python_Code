import pytest


@pytest.mark.smoke
def test_string_assert():
    s = "Pycharm"
    assert s == "Pycharm"


def test_expression_assert():
    a = 5
    b = 6
    assert a + 1 == b, "Value does not addup"
