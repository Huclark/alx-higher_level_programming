#!/usr/bin/python3

"""
print_reversed_list_integer - Prints all integers of a list, in reverse order.
"""


def print_reversed_list_integer(my_list=[]):
    if not my_list:
        return

    else:
        my_list.reverse()

    for number in range(len(my_list)):
        print("{:d}".format(my_list[number]))
