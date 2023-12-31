#!/usr/bin/python3
"""
Square Module
"""
from models.base import *
from models.rectangle import *


class Square(Rectangle):
    """
    Square Class that inherits from Rectangle
    """
    def __init__(self, size, x=0, y=0, id=None):
        """
        initialization of the Square Class
        """
        super().__init__(size, size, x, y, id)

    @property
    def size(self):
        """
        size getter
        """
        return self.width

    @size.setter
    def size(self, value):
        """
        size setter
        """
        if type(value) is not int:
            raise TypeError("width must be an integer")
        if value <= 0:
            raise ValueError("width must be > 0")
        self.width = value
        self.height = value

    def __str__(self):
        """
        string representation of the Square Class
        """
        return "[Square] ({}) {}/{} - {}".format(
                        self.id, self.x, self.y, self.width)

    def update(self, *args, **kwargs):
        """
        update method
        """
        if args:
            if len(args) >= 1:
                self.id = args[0]
            if len(args) >= 2:
                self.size = args[1]
            if len(args) >= 3:
                self.x = args[2]
            if len(args) >= 4:
                self.y = args[3]
        else:
            for key, value in kwargs.items():
                if key == "id":
                    self.id = value
                if key == "size":
                    self.size = value
                if key == "x":
                    self.x = value
                if key == "y":
                    self.y = value

    def to_dictionary(self):
        """
        dictionary representation of the Square Class
        """
        return {
            "id": self.id,
            "size": self.width,
            "x": self.x,
            "y": self.y
        }
