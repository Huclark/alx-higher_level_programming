#!/usr/bin//python3

"""
no_c - Removes all characters c and C from a string.
"""


def no_c(my_string):
    if not my_string:
        return

    new_str = ""

    for letter in my_string:
        if letter not in "Cc":
            new_str += letter

    return new_str
