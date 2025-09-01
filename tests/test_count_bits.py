import pytest
from challenges.count_bits import count_bits

@pytest.mark.parametrize('input', [
    'string',
    None,
    2.37,
    [],
    {},
    True,
    False,
])
def test_input(input):
    with pytest.raises(TypeError, match='Integer input only'):
        count_bits(input)

@pytest.mark.parametrize('input, expected', [
    (-100, 3),
    (-1, 1),
    (0, 0),
    (7, 3),
    (9, 2),
    (10, 2),
    (100, 3),
    (149, 4),
    (1234, 5),
    ((10*100000000), 13)
])
def test_result(input, expected):
    assert count_bits(input) == expected

