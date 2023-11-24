#!/usr/bin/python3
"""Returns the division of a list of lists
by a number (float or integer)
"""
def matrix_divided(matrix, div):
    """Divides all elements of a list of lists

    Args:
        matrix (int, float): A list of lists to divide by div
        div (int, float): Number (float or int) to divide the list by

    Returns:
        list: A new matrix (list)
    """
    if not isinstance(matrix, list):
        raise TypeError("matrix must be a matrix (list of lists) of integers/floats")
    if any(not row for row in matrix):
        raise TypeError ("matrix must be a matrix (list of lists) of integers/floats")
    if any(len(row) != len(matrix[0]) for row in matrix):
        raise TypeError("Each row of the matrix must have the same size")

    if not isinstance(div, (int, float)) or isinstance(div, bool):
        raise TypeError("div must be a number")

    if div == 0:
        raise ZeroDivisionError("division by zero")

    new_matrix = []

    for idx in range(len(matrix)):
        new_list = []
        for i in range(len(matrix[idx])):
            if not isinstance(matrix[idx][i], (int, float)) or isinstance(matrix[idx][i], bool):
                raise TypeError("matrix must be a matrix (list of lists) of integers/floats")
            result = round(float(matrix[idx][i] / div), 2)
            new_list.append(result)
        new_matrix.append(new_list)
            
    return new_matrix
