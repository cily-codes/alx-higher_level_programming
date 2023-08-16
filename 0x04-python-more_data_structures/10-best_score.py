#!/usr/bin/python3
def best_score(a_dictionary):
    """returns a key with the biggest integer value"""
    if a_dictionary is None:
        return (None)

    b_score = max(a_dictionary.values(), default=None)
    for k, v in a_dictionary.items():
        if v == b_score:
            return (k)
