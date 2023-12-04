#!/usr/bin/python3
"""
11. Square Module #2

"""
Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """
    Class Square
    """

    def __init__(self, size):
        """
        Class constructor/ initializer

        Args:
            size (int): size
        """
        self.integer_validator("size", size)
        self.__size = size
        super().__init__(self.__size, self.__size)

    def area(self):
        """
        Public Instance method that returns the area
        """
        return (self.__size ** 2)

    def __str__(self):
        """
        String representation of the class
        """
        return ("[Square] {}/{}".format(self.__size, self.__size))
