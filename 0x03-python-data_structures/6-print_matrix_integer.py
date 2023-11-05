#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):
    """Prints a matrix of integers"""
    for each_list in matrix:
        new_list = ""
        for item in each_list:
            new_list += str(item) + " "
        new_list = new_list.rstrip()
        print("{}".format(new_list))
