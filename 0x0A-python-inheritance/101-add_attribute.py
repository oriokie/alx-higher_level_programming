#!/usr/bin/python3
"""
13. Can I?

"""


def add_attribute(obj, attr, value):
    """
    Function that adds a new attribute to an object if it’s possible

    Args:
        obj: object
        attr: attribute
        value: value
    """
    if not hasattr(obj, "__dict__"):
        raise TypeError("can't add new attribute")
    setattr(obj, attr, value)
