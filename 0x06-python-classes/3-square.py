#!/usr/bin/python3
""" This is a square Class  """


class Square:
    """
    Class that defines a square

    Attributes:
        size (int): the dimension of the square

    """
    def __init__(self, size=0):
        """
        initialization of the class

        Args:
            __size (int): the dimension of the square

        """
        self.__set_size(size)

    def __set_size(self, size):
        """
        Validates the size

        Args:
            size: size of the square

        Raises:
            TypeError: if the size is not an integer
            ValueError: if size is less than zero

        """
        if type(size) is not int:
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = size

    def area(self):
        """
        A method that returns the area of a square

        Returns:
            integer: the area of the square
        """
        return self.__size**2
