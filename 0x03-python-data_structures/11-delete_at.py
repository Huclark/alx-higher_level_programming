#!/usr/bin/python3
def delete_at(my_list=[], idx=0):
    """Deletes the item at a specific position in a list
    and returns the newly modified list
    """
    if idx >= 0 and idx < len(my_list):
        del my_list[idx]

    return my_list
