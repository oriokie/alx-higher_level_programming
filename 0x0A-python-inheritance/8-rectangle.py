#!/usr/bin/python3
"""
    8. Rectangle
"""
BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    """
    Class Rectangle
    """

    def __init__(self, width, height):
        """
        Class constructor/ initializer

        Args:
            width (int): width
            height (int): height
        """
        self.integer_validator("width", width)
        self.__width = width
        self.integer_validator("height", height)
        self.__height = height
