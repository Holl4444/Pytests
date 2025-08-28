from math import sqrt

# True is considered an instance of int as bool is a subclass of int @:O
def is_square(n: int) -> bool:
    if not isinstance(n, int) or isinstance(n, bool):
        raise TypeError('Integer inputs only')
    if n < 0:
        return False
    if n == sqrt(n) ** 2:
        return True
    return False
