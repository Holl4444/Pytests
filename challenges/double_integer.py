def double_integer(i: int):
    if not isinstance(i, int):
        raise TypeError('Integer input only')
    return i * 2
    