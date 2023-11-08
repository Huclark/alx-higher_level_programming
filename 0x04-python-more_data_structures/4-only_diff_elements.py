#!/usr/bin/python3

def only_diff_elements(set_1, set_2):
    """Returns a set of all elements
    present in only one set

    set_1 is the first set
    set_2 is the second set
    """
    od_set = set()

    for item1 in set_1:
        if item1 not in set_2:
            od_set.add(item1)

    for item2 in set_2:
        if item2 not in set_1:
            od_set.add(item2)

    return od_set
