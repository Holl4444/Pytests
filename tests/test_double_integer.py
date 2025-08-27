import pytest
from challenges.double_integer import double_integer

def test_valid_input():
    with pytest.raises(TypeError, match='Integer input only'):
        double_integer('string')
    with pytest.raises(TypeError, match='Integer input only'):
        double_integer(2.5)     

@pytest.mark.parametrize('i, expected', [
    (-3, -6), (-6, -12), (0, 0), (1, 2), (2, 4), (5, 10), (8, 16), (13, 26), (28, 56), (1000, 2000), (10**10, 10,000,000,000), (10**18, 1,000,000,000,000,000,000)])

def test_return_value(i: int, expected: int):
    assert double_integer(i) == expected