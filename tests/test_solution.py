from challenges.solution import solution
import pytest

@pytest.mark.parametrize('input1, input2', [
    (24, 24),
    ('hello', 24),
    (24, 'world'),
    (None, 'test')
])

def test_input_type (input1, input2):
    with pytest.raises(TypeError, match='String inputs only'):
        solution(input1, input2)

def test_output_type():
    assert isinstance(solution('qwe', 'we'), bool)
    assert isinstance(solution('qwe', 'te'), bool)

@pytest.mark.parametrize('input1, input2, expected', [
    ('rabbit', 'bbit', True),
    ('rabbit', 'ait', False),
    ('rabbit', 'rabbit', True),
    ('rabbit', 't', True),
    ('rabbit', 'r', False)
])
def test_reports_correctly(input1, input2, expected):
    assert solution(input1, input2) == expected

# $ pytest --cov=challenges tests/
# ================================================================ test session starts ================================================================
# platform win32 -- Python 3.13.7, pytest-8.4.1, pluggy-1.6.0
# rootdir: C:\Users\holly\repos\Pytests
# plugins: cov-6.2.1
# collected 10 items

# tests\test_solution.py ..........                                                                                                              [100%]

# ================================================================== tests coverage =================================================================== 
# __________________________________________________ coverage: platform win32, python 3.13.7-final-0 __________________________________________________ 

# Name                     Stmts   Miss  Cover
# --------------------------------------------
# challenges\__init__.py       0      0   100%
# challenges\solution.py       4      0   100%
# --------------------------------------------
# TOTAL                        4      0   100%
# ================================================================ 10 passed in 0.07s =================================================================
# (.venv)