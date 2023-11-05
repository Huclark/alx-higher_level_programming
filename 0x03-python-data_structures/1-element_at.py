#!/usr/bin/python3

"""
element_at - Retrieves an element from a list like in C
"""


def element_at(my_list, idx):
    if len(my_list) >= idx < 0:
        return None
    else:
        return my_list[idx]
