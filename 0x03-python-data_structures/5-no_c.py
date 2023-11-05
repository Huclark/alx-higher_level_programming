#!/usr/bin//python3

"""
no_c - Removes all characters c and C from a string.
"""


def no_c(my_string):
    if not my_string:
        return

    new_str = ""

    for i in range(len(my_string)):
        if my_string[i] != 'c' and my_string[i] != 'C':
            new_str += my_string[i]

    return new_str
