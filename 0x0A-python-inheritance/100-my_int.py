#!/urs/bin/python3
"""Demonstrates the MyInt subclass
"""


class MyInt(int):
    """Creating a child class of the built-in int
    class

    Args:
        int (int): The built-in int class
    """
    def __eq__(self, other):
        """Inverts the == operator to !=
        """
        return super().__ne__(other)

    def __ne__(self, other):
        return super().__eq__(other)
