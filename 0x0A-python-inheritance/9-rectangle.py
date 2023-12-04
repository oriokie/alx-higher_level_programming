#!/usr/bin/python3
"""
    9. Full Rectangle
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

    def area(self):
        """
        Public Instance method that returns the area
        """
        return (self.__width * self.__height)

    def __str__(self):
        """
        String representation of the class
        """
        return ("[Rectangle] {}/{}".format(self.__width, self.__height))
