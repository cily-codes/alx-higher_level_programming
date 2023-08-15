#!/usr/bin/python3
def max_integer(my_list=[]):
    """Finds the biggest integer of a list"""
    if not my_list:
        return (None)

    max_n = min(my_list)
    for i in my_list:
        if i > max_n:
            max_n = i

    return (max_n)
