#!/usr/bin/python3

def safe_print_list(my_list=[], x=0):
    """Prints x elements of a list, where x represents the number of
    elements to print.

    Args:
        my_list: List to print. Can contain any data type.
        x: Number of elements to print.
    """
    no_of_elements = 0

    try:
        for idx in range(x):
            print(my_list[idx], end="")
            no_of_elements += 1
    except IndexError:
        pass
    finally:
        print()
    return no_of_elements
