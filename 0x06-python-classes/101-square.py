#!/usr/bin/python3
""" This is a square Class  """


class Square:
    """
    Class that defines a square

    Attributes:
        size (int): the dimension of the square
        position (tuple): the position of the square

    """
    def __init__(self, size=0, position=(0, 0)):
        """
        initialization of the class

        Args:
            size (int): the dimension of the square
            position (tuple): a tuple of the position of the square

        """
        self.size = size
        self.position = position

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

    @property
    def position(self):
        """
        Getter of the position attribute
        """
        return self.__position

    @position.setter
    def position(self, value):
        """
        Setter of position attribute

        Args:
            value (tuple): the position of the square

        Raises:
            TypeError: if tuple does not have 2 positive integers

        """
        if not type(value) is tuple:
            raise TypeError("position must be a tuple of 2 positive integers")
        elif len(value) != 2:
            raise TypeError("position must be a tuple of 2 positive integers")
        elif type(value[0]) is not int or type(value[1]) is not int:
            raise TypeError("position must be a tuple of 2 positive integers")
        elif value[0] < 0 or value[1] < 0:
            raise TypeError("position must be a tuple of 2 positive integers")
        else:
            self.__position = value

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
            print('\n'*self.__position[1], end="")
            for i in range(0, self.__size):
                print(" "*self.__position[0], end="")
                print("#"*self.__size)

    def __str__(self):
        """
        String representation of the square

        """
        if self.__size == 0:
            return "\n"
        else:
            return "\n".join([" " * self.__position[0] + "#" * self.__size
                              for i in range(self.__size)])
