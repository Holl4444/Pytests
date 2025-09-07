from challenges.move_zeros import move_zeros
import pytest

def test_same_length():
    lst = [1, 2, 3, 0, 4, 0, 5]
    assert len(move_zeros(lst)) == len(lst)

def test_only_integers():
    lst = [1, 2, 3, 4, 5]
    assert move_zeros(lst) == lst

def test_zeros_only_at_end():
    lst = [1, 2, 3, 0, 4, 0, 5]
    returned_lst = move_zeros(lst)
    trailing_zeros = returned_lst[returned_lst.index(0):]
    cleaned_returned_lst = returned_lst[:returned_lst.index(0)]
    assert cleaned_returned_lst.count(0) == 0
    assert trailing_zeros.count(0) == len(trailing_zeros)

@pytest.mark.parametrize('lst, result', [
    ([1, 4, 0, 3, 8], [1, 4, 3, 8, 0]),
    ([0, 0, 2, 3, 4], [2, 3, 4, 0, 0]),
    ([0, 2, 9, 2, 4,  0, 1, 5, 0], [2, 9, 2, 4, 1, 5, 0, 0, 0])
])
def test_functionality(lst, result):
    assert move_zeros(lst) == result

@pytest.mark.parametrize('input', [
    {1: 1, 2: 1},
    'hesitate',
    None,
    0,
    4,
    str([1, 2, 3, 4])
])
def test_valid_input(input):
    with pytest.raises(TypeError, match='Input must be in the form of a list'):
        move_zeros(input)

def test_empty_list():
    assert move_zeros([]) == []

def test_single_non_zero():
    assert move_zeros([2]) == [2]

def test_single_zero():
    assert move_zeros([0]) == [0]

def test_all_zeros():
    assert move_zeros([0, 0, 0, 0, 0]) == [0, 0, 0, 0, 0]

def test_keeps_bools():
    assert move_zeros([1, True, 5, 0, False, 6, 2]) == [1, True, 5, False, 6, 2, 0]

def test_false_position():
    assert move_zeros([1, False, 0, True]) == [1, False, True, 0]

def test_many_data_types():
    assert move_zeros(['hello', 0, 1, 4, 'world', ['jungle', 'boogie'], 6, {'a': 9}, 7.8]) == ['hello', 1, 4, 'world', ['jungle', 'boogie'], 6, {'a': 9}, 7.8, 0]

def test_zero_as_float():
    assert move_zeros([1, 0.0, 2]) == [1, 2, 0.0]