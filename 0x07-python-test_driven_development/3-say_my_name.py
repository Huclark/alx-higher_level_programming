#!/usr/bin/python3
"""Prints 'My name is <first name> <last name>'
to stdout
"""


def say_my_name(first_name, last_name=""):
    """Prints 'My name is <first name> <last name> to
    stdout

    Args:
        first_name (str): First name of user
        last_name (str, optional): Last name of user. Defaults to "".
    """
    if not isinstance(first_name, str):
        raise TypeError("first_name must be a string")
    if not first_name:
        raise ValueError

    if not isinstance(last_name, str):
        raise TypeError("last_name must be a string")

    print("My name is {} {}".format(first_name.strip(), last_name.strip()))
