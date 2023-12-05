#!/usr/bin/python3
"""A function that demonstrates JSON implementation
"""


import json


def from_json_string(my_str):
    """Returns an object (python data structure) represented
    by a JSON string

    Args:
        my_str (str): String

    Returns:
        object: An object represented by JSON string
    """
    return json.loads(my_str)
