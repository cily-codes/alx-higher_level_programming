#!/usr/bin/python3
import sys

args = sys.argv
len_args = len(args)
total = 0

if __name__ == '__main__':

    if len_args > 1:
        for i in range(1, len_args):
            total += int(args[i])

    print(total)
