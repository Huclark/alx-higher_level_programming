#!/usr/bin/python3
"""A function that demonstrates JSON implementation
"""


import json

def to_json_string(my_obj):
    """Returns an object(python data structure) represented
    by a JSON string

    Args:
        my_obj (object): Object to be represented by a JSON string

    Returns:
        object: An object represented by a JSON string
    """
    return json.dumps(my_obj)
