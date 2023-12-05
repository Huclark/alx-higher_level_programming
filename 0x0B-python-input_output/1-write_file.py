#!/usr/bin/python3
"""A function that demonstrates file handling
"""


def write_file(filename="", text=""):
    """Writes a string to a text file using encoding="utf-8"

    Args:
        filename (str, optional): Name of file. Defaults to "".
        text (str, optional): Text to input. Defaults to "".

    Returns:
        int: Number of characters actually read and printed
    """
    if not filename:
        return
    with open(filename, "w", encoding="utf-8") as f:
        return f.write(text)
