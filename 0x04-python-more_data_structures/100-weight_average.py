#!/usr/bin/python3
def weight_average(my_list=[]):
    """Returns the weighted average of all integers
    tuple (<score>, <weight>)
    Returns 0 if the list is empty
    """
    if not my_list:
        return 0

    total_mul = 0
    total_num = 0

    for tuple in my_list:
        total_mul += tuple[0] * tuple[1]
        total_num += tuple[1]

    return total_mul / total_num
