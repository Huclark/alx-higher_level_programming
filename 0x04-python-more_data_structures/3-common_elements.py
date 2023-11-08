#!/usr/bin/python3
def common_elements(set_1, set_2):
    """Returns a set of common elements in two sets
    
    set_1 is the first set
    set_2 is the second set
    """
    c_set = set()

    for item1 in set_1:
        for item2 in set_2:
            if item1 == item2:
                c_set.add(item1)

    return c_set
