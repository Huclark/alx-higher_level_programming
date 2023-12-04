#!/urs/bin/python3
"""Demonstrates the MyInt subclass
"""


class MyInt(int):
    """Creating a child class of the built-in int
    class

    Args:
        int (int): The built-in int class
    """
    def __eq__(self, value):
        """Inverts the == operator to !=
        """
        return self.real != value

    def __ne__(self, value):
        """Inveryts the != operator to ==
        """
        return self.real == value
