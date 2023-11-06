#!/usr/bin/python3
def max_integer(my_list=[]):
    """Finds amd returns the biggest number of a list"""
    if len(my_list) == 0:
        return None
    biggest_num = my_list[0]
    for i in range(len(my_list)):
        if my_list[i] > biggest_num:
            biggest_num = my_list[i]
    return biggest_num
