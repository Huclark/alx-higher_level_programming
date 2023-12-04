#!/usr/bin/python3
"""A python program that demonstrates classes and inheritance"""


def is_kind_of_class(obj, a_class):
    """Checks if an object is an instance of a specified class or
    a class that inherited from a specified class

    Args:
        obj: The object to inspect
        a_class: The class to match

    Returns:
        bool: True if there is a match or False if otherwise
    """
    return type(obj) is a_class or issubclass(type(obj), a_class)
