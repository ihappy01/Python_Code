import pytest

@pytest.mark.parametrize(
    "Test_name,value1,value2",
    [
        ('Add_interger',6,7),
        ('Add_float',5.7,9.3)
    ]
)
def test_add_function(Test_name,value1,value2):
    print(f"The addition of {value1} and {value2} is {value1+value2}")