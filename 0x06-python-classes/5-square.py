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
            size (int): the dimension of the square

        """
        self.size = size

    @property
    def size(self):
        """
        Getter method

        """
        return self.__size

    @size.setter
    def size(self, value):
        """
        Validates the size & Setter of the instance attributes

        Args:
            value: size of the square

        Raises:
            TypeError: if the value is not an integer
            ValueError: if value is less than zero

        """
        if type(value) is not int:
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = value

    def area(self):
        """
        A method that returns the area of a square

        Returns:
            integer: the area of the square
        """
        return self.__size**2

    def my_print(self):
        """
        Method that prints a square using the symbol #

        """
        if self.__size == 0:
            print()
        else:
            for i in range(self.__size):
                print("#"*self.__size)
