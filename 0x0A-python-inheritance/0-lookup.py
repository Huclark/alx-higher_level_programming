#!/usr/bin/python3
"""Returns the list of available attributes
and methods of an object
"""


def lookup(obj):
    """Returns a list of objects

    Args:
        obj (_type_): The object to inspect.

    Returns:
        list: A list of strings representing attributes and methods
    """
    # Use dir() to retrieve the list of available attributes and methods
    return dir(obj)
