
def move_zeros(lst):
    if not isinstance(lst, list):
        raise TypeError('Input must be in the form of a list')
    # Keeps boolean values if the list is more than just integers ie. [2, 4, 0, False, 1, True, 8, 0]
    new_list = [x for x in lst if isinstance(x, bool) or x != 0]
    return new_list + [0] * (len(lst) - len(new_list))



if __name__ == '__main__':
    move_zeros([9, 0, 0, 9, 1, 2, 0, 1, 0, 1, 0, 3, 0, 1, 9, 0, 0, 0, 0, 9])