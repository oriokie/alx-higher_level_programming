#!/usr/bin/python3
"""
Module for printing a square

"""


def print_square(size):
    """
    Function that prints a square with the character #
    Importation of any module not allowed

    Args:
        size: size of the square

    Raises:
        TypeError: if size is not an integer
        ValueError: if size is less than 0
        TypeError: if size is a float

    """
    if type(size) is not int:
        raise TypeError("size must be an integer")
    if size < 0:
        raise ValueError("size must be >= 0")
    if size == 0:
        print()
    else:
        for i in range(size):
            print("#" * size)
