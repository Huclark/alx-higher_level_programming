#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
    """Computes and returns the square value
    of all integers of a matrix
    """
    squared_matrix = []

    for matrix_idx in range(len(matrix)):
        squared_list = []

        for list_idx in range(len(matrix[matrix_idx])):
            list_value = matrix[matrix_idx][list_idx]
            squared_list.append(list_value ** 2)

        squared_matrix.append(squared_list)

    return squared_matrix
