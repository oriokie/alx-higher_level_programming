#!/usr/bin/python3
"""
Same class or inherit from

"""


def is_kind_of_class(obj, a_class):
    """
    Function that returns True if the object is exactly an instance of
    the specified class ; otherwise False

    Args:
        obj: object
        a_class: class

    Returns:
        True if the object is exactly an instance of the specified class
        otherwise False

    """
    return isinstance(obj, a_class)
