#!/usr/bin/python3
"""A function that demonstrates JSON implementation
"""


import json


def load_from_json_file(filename):
    """Creates an object from a JSON file

    Args:
        filename (str): Name of JSON file

    Returns:
        object: Object from JSON file
    """
    with open(filename, encoding="utf-8") as file:
        return json.load(file)
