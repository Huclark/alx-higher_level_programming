#!/usr/bin/python3
def max_integer(my_list=[]):
    """Finds amd returns the biggest number of a list"""
    if list == []:
        return None
    biggest_num = my_list[0]
    for number in my_list:
        if number > biggest_num:
            biggest_num = number
    return biggest_num
