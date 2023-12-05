#!/usr/bin/python3
"""A function that demonstrates file handling
"""


def append_write(filename="", text=""):
    """Appends a string at the end of a text file
    using encoding=utf-8

    Args:
        filename (str, optional): Name of file. Defaults to "".
        text (str, optional): Text to append to file. Defaults to "".

    Returns:
        int: Number of characters written to file
    """
    if not filename:
        return 0 # return immediately if string is empty
    with open(filename, "a", encoding="utf-8") as file:
        return file.write(text)
