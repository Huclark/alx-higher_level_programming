#!/usr/bin/python3
"""A python program to demonstrate inheritance
"""


class MyList(list):
    """Creating a child class of the built-in list
    class

    Args:
        list (list): The built-in list class
    """
    def print_sorted(self):
        """Prints a sorted list in ascending order
        """
        print(sorted(self))
