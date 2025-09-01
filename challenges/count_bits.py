def count_bits(n):
    # Check positive integer - bools are sub class of integer ... sneaky
    if not isinstance(n, int) or isinstance(n, bool):
        raise TypeError('Integer input only')
    # Find binary
    binary = bin(n)[2:]
    # count the '1's
    return binary.count('1')

print(bin(10*100000000))