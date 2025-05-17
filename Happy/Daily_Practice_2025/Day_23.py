


print (set({'Hacker' : 'DOSHI', 'Rank' : 616 }))

# print(s)

import pytest

@pytest.mark.parametrize('a,b',
                         [
                             (2,3),
                             (4,5),
                             (5,6)])
def test_addition(a,b):
 print(f"The addition of the function is {a}+{b} is {a+b}")

