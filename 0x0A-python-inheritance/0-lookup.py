#!/usr/bin/python3
"""
    Write a function that returns the list of available attributes and methods
    of an object:
    Prototype: def lookup(obj):
    Returns a list object
"""


def lookup(obj):
    """
    Function to lookup all the available attributes and methods of a class

    Args:
        obj: object class

    Returns: list of objects
    """
    return dir(obj)
