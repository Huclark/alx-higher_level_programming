#!/usr/bin/python3
"""A function that demonstrates class and inheritance"""


def inherits_from(obj, a_class):
    """Checks if an object is an instance of a class that
    inherited (directly or indirectly) from the specified class

    Args:
        obj: Object to check
        a_class: Class to match

    Returns:
        bool: True if object is a match or False if otherwise
    """
    return type(obj) is not a_class and isinstance(obj, a_class)
