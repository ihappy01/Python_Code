import pytest

@pytest.mark.parametrize("a,b",[(2,4)
                                ,(2,2)
                                ,(5,2)])
def test_true(a,b):
    assert a == b,"Variables are not equal"