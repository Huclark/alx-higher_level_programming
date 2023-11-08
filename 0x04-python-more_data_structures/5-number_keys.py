#!/usr/bin/python3

def number_keys(a_dictionary):
    """Returns the number of keys in a dictionary

    a_dictionary is the dictionary passed to the function
    """
    no_of_keys = 0

    for _ in a_dictionary:
        no_of_keys += 1

    return no_of_keys
