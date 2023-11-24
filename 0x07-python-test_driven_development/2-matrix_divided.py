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
    # if matrix is not a list or a list with an empty list(s)
    if not isinstance(matrix, list) or any(not row for row in matrix):
        raise TypeError("matrix must be a matrix (list of lists) of "
                        "integers/floats")
    # Check if all lists in matrix have equal sizes
    if any(len(row) != len(matrix[0]) for row in matrix):
        raise TypeError("Each row of the matrix must have the same size")
    # Check if divisor is not an int or float data type
    if not isinstance(div, (int, float)) or isinstance(div, bool):
        raise TypeError("div must be a number")
    # Handle division by zero
    if div == 0:
        raise ZeroDivisionError("division by zero")

    new_matrix = []

    # Loop through matrix to access each list
    for idx in range(len(matrix)):
        new_list = []
        # Loop through each list in matrix and divide by div
        for i in range(len(matrix[idx])):
            # Inspect if each list element is an int or float data type
            if (not isinstance(matrix[idx][i], (int, float)) or
                    isinstance(matrix[idx][i], bool)):
                raise TypeError("matrix must be a matrix (list of lists) "
                                "of integers/floats")
            # Divide each element in list and append result to new list
            result = round(float(matrix[idx][i] / div), 2)
            new_list.append(result)
        # Append each divided list to new matrix
        new_matrix.append(new_list)

    return new_matrix
