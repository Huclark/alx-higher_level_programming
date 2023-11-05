#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):
    """ Prints a matrix of integers """
    for idx1 in range(len(matrix)):
        for idx2 in range(len(matrix[idx1])):
            if idx2 != 0:
                print(" ", end="")
            print("{:d}".format(matrix[idx1][idx2]), end="")
        print()
