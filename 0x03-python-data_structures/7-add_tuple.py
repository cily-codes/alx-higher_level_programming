#!/usr/bin/python3
def add_tuple(tuple_a=(), tuple_b=()):
    """Addition of 2 tuples"""
    a = auth_tuple(tuple_a)
    b = auth_tuple(tuple_b)

    return ((a[0] + b[0]), (a[1] + b[1]))


def auth_tuple(_tuple=()):
    if len(_tuple) < 2:
        if len(_tuple) == 1:
            _tuple = (_tuple[0], 0)
        elif len(_tuple) == 0:
            _tuple = (0, 0)
    elif len(_tuple) > 2:
        _tuple = (_tuple[0], _tuple[1])

    return (_tuple)
