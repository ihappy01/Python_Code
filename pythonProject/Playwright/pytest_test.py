
def test_1():
    x=10
    y=10
    assert x==y

def test_2():
    name="Selenium"
    title="Selenium is for web automation"
    assert name in title

def test_3():
    name="Jenkins"
    title="Jenkins "
    assert name in title,"Title does not match"