import pytest
from challenges.is_square import is_square

@pytest.mark.parametrize('num, result', [
    (-1, False),
    (0, True),
    (3, False),
    (9, True),
    (13, False),
    (4, True),
    (25, True),
    (26, False),
    (10**8, True),
    (10**8 + 1, False)
])

def test_correctly_identifies_squares(num, result):
    assert is_square(num) == result

@pytest.mark.parametrize('input', [
    'string',
    [1, 2, 3],
    None,
    True
])

def test_input(input):
    with pytest.raises(TypeError, match='Integer inputs only'):
        is_square(input)