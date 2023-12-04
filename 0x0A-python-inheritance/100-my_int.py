#!/usr/bin/python3
"""
12. My integer

Write a class MyInt that inherits from int:

MyInt is a rebel. MyInt has == and != operators inverted
You are not allowed to import any module

"""


class MyInt(int):
    """
    Class MyInt that inherits from int
    """

    def __eq__(self, other):
        """
        Function that returns True if self != other
        """
        return self.real != other

    def __ne__(self, other):
        """
        Function that returns True if self == other
        """
        return self.real == other
