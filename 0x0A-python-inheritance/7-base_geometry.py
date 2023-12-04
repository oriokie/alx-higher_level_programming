#!/usr/bin/python3
"""
7. Integer validator

"""


class BaseGeometry:
    """
    Class BaseGeometry
    """
    def area(self):
        """
        Public Instance method
        Function that raise Exception: area() is not implemented
        """
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """
        Function that validates an integer

        Args:
            name (str): name
            value (int): value
        """
        if type(value) is not int:
            raise TypeError("{} must be an integer".format(name))
        if value <= 0:
            raise ValueError("{} must be greater than 0".format(name))
