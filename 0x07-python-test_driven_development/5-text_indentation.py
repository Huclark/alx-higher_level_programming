#!/usr/bin/python3
"""Defines a text indentation function
"""


def text_indentation(text):
    """Prints a text with 2 new lines after each of these characters:
    ".", "?" and ":".

    Args:
        text (str): The string to indent

    Raises:
        TypeError: text must be a string
    """
    if not isinstance(text, str):
        raise TypeError("text must be a string")

    flag = True
    for i in range(len(text)):
        if i + 1 < len(text):
            if (text[i - 1] == "\n" or text[i + 1] == "\n") and text[i] == " ":
                flag = True
                continue
        if flag:
            if text[i] == " ":
                continue
            else:
                flag = False
        if text[i] in ".?:":
            flag = 1
            print("{}\n".format(text[i]))
        else:
            print(text[i], end="")
            if text[i] == "\n" and text[i + 1] == " ":
                flag = True
