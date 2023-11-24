#!/usr/bin/python3
"""
Module 2-matrix_divided
Contains function that divides all elements of a matrix
Prototype: def matrix_divided(matrix, div):

"""


def matrix_divided(matrix, div):
    """
    Function that divides all the elements of a matrix
    Matrix must be a list of lists of integers or floats.
    Each row of the matrix must be of the same size
    Div must be a number (integer or float)
    Div cant be zero

    Args:
        matrix: list of lists of integers or floats
        div: integer or float

    Raise:
        TypeError: matrix must be a matrix (list of lists) of integers/floats
        TypeError: Each row of the matrix must have the same size
        TypeError: div must be a number
        ZeroDivisionError: div can't be 0

    """
    T_error = "matrix must be a matrix (list of lists) of integers/floats"

    if not isinstance(div, (int, float)):
        raise TypeError("div must be a number")

    if div == 0:
        raise ZeroDivisionError("division by zero")

    if type(matrix) is not list or matrix == [] or \
            matrix[0] == []:
        raise TypeError(T_error)

    if not all(isinstance(row, list) for row in matrix):
        raise TypeError(T_error)

    if not all((isinstance(num, (int, float)) for row in matrix
                for num in row)):
        raise TypeError(T_error)

    if not all(len(row) == len(matrix[0]) for row in matrix):
        raise TypeError("Each row of the matrix must have the same size")

    return [[round(num / div, 2) for num in row] for row in matrix]
