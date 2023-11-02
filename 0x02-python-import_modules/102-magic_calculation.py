#!/usr/bin/python3

"""This function does exactly the same as the bytecode in
the bytecode102 file
"""


def magic_calculation(a, b):

    from magic_calculation_102 import add, sub

    if a < b:
        c = add(a, b)
        for i in range(4, 6):
            c = add(c, i)
        return c
    else:
        return sub(a, b)
