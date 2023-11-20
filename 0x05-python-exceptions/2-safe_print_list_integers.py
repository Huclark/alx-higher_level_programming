#!/usr/bin/python3

def safe_print_list_integers(my_list=[], x=0):
    """Prints the first x elements of a list and only integers

    Args:
        my_list: List to print(integer, string, etc.)
        x: Number of elements to print

    Return: The real number of elements to access in my_list
    """
    count = 0

    for idx in range(x):
        try:
            print("{:d}".format(my_list[idx]), end="")
            count += 1
        except (IndexError, ValueError):
            pass
    print()
    return count
            