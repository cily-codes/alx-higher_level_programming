#!/usr/bin/python3
from add_0 import add

a = 1
b = 2

if __name__ == "__main__":

    """
    Prints the result of the addition of two numbers
    """

    print("{:d} + {:d} = {:d}".format(a, b, add(a, b)))
