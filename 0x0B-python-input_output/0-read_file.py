#!/usr/bin/python3
"""A function that demonstrates file handling"""


def read_file(filename=""):
    """Reads a text file using encoding="utf-8"

    Args:
        filename (str, optional): The name of file to read from
        represented as a string. Defaults to "".
    """
    with open(filename, encoding="utf-8") as f:
        for line in f:
            print(line, end="")
