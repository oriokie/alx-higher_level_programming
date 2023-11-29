#!/usr/bin/python3

"""
Rectangle class that defines a rectangle by: (based on 0-rectangle.py)
Instantiation with optional width and height:

def __init__(self, width=0, height=0):

"""


class Rectangle:
    """
    The Rectangle Class

    Attributes:
        width (int): The width of the rectangle
        height (int): The height of the rectangle
        no_of_instance: number of instances

    """
    number_of_instances = 0
    print_symbol = "#"

    def __init__(self, width=0, height=0):
        """
        initializing the rectangle

        Args:
            width (int): The width of the rectangle
            height (int): The height of the rectangle

        """
        self.width = width
        self.height = height
        Rectangle.number_of_instances += 1

    @property
    def width(self):
        """Getter: widht of the rectangle"""
        return self.__width

    @width.setter
    def width(self, value):
        """
        Setter: width of the rectangle

        Args:
            value (int): The width of the rectangle

        Raises:
            TypeError: if width is not an integer
            ValueError: if width is less than 0
        """
        if type(value) is not int:
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        """Getter: height of the rectangle"""
        return self.__height

    @height.setter
    def height(self, value):
        """
        Setter: height of the rectangle

        Args:
            value (int): The height of the rectangle
        """
        if type(value) is not int:
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    def area(self):
        """Returns the rectangle area"""
        return self.__width * self.__height

    def perimeter(self):
        """Returns the rectangle perimeter"""
        if self.__width == 0 or self.__height == 0:
            return 0
        return 2 * (self.__width + self.__height)

    def __str__(self):
        """Returns the printable representation of the rectangle"""
        if self.__width == 0 or self.__height == 0:
            return ""
        character = str(self.print_symbol)
        return ((character*self.__width + "\n")*self.__height)[:-1]

    def __repr__(self):
        """Returns the string representation of the rectangle"""
        return "Rectangle({:d}, {:d})".format(self.__width, self.__height)

    def __del__(self):
        """Prints a message when an instance of Rectangle is deleted"""
        Rectangle.number_of_instances -= 1
        print("Bye rectangle...")
