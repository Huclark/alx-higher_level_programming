#!/usr/bin/python3
"""A python program that demonstrates classes"""


def is_same_class(obj, a_class):
    """Checks if an object is an instance of a specified class

    Args:
        obj: The object to inspect
        a_class: The class to match

    Returns:
        Bool: True if object is an instance of specified class
        otherwise return False
    """
    return type(obj) is a_class
