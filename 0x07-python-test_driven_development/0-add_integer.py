#!/usr/bin/python3
"""
This module adds two integers:
    a and b must be integers or floats
    a and b must be first casted to integers if they are float
    No other module should be imported
"""


def add_integer(a, b=98):
    """
    This function adds two integers.

    Args:
        a (int or float): The first number
        b (int or float): The second number. The default value is 98

    Raises:
        TypeError: if a or b is not an integer or float

    Returns:
        int: the addition of a and b

    """
    if type(a) not in [int, float]:
        raise TypeError("a must be an integer")
    if type(b) not in [int, float]:
        raise TypeError("b must be an integer")
    result = int(a) + int(b)
    if result == float('inf') or result == -float('inf'):
        raise OverflowError
    return int(result)
