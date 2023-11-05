#!/usr/bin/python3

"""
element_at - Retrieves an element from a list like in C
"""


def element_at(my_list, idx):
    if idx >= len(my_list) or idx < 0:
        return None

    return my_list[idx]
