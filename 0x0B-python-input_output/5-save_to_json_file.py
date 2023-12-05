#!/usr/bin/python3
"""A funtion that demonstrates JSON implementation
"""


import json


def save_to_json_file(my_obj, filename):
    """Writes an object to a text file using a JSON representation

    Args:
        my_obj (object): Object to write into file
        filename (str): File name
    """
    with open(filename, "w+", encoding="utf-8") as file:
        json.dump(my_obj, file)
