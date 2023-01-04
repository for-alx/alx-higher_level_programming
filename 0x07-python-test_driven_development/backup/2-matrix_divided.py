#!/usr/bin/python3

"""
This is the 2-matrix_divided module.
It contains 1 function: matrix_divided(matrix, div)
"""


def matrix_divided(matrix, div):
    """
        Function that divides all elements of a matrix.

        Args:
            matrix(list): List of 2 dimensional matrix
            div (int/float): Divider number

        Returns:
            returns a new matrix where all elements have been divided by div
    """
    result = []

    if type(div) != float and type(div) != int:
        raise TypeError("div must be a number")

    elif div == 0:
        raise ZeroDivisionError("division by zero")

    if len(matrix[0]) != len(matrix[1]):
        raise TypeError("Each row of the matrix must have the same size")

    for i in matrix:
        temp = []
        for j in i:
            if type(j) != float and type(j) != int:
                raise TypeError("matrix must be a matrix(list of lists) of \
integers/floats")
            # print(j) #For test
            temp.append(round(j / div, 2))
        result.append(temp)

    return result
