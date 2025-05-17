import time
import pytest

def test_1():
    a=2
    time.sleep(2)
    assert 2==a

def test_2():
    a=3
    time.sleep(2)
    assert 3==a

def test_3():
    a=4
    time.sleep(2)
    assert 4==a

def test_4():
    a=5
    time.sleep(2)
    assert 5==a

def test_5():
    a=6
    time.sleep(2)
    assert 6==a