#!/usr/bin/python3
"""
    MyList Module

"""


class MyList(list):
    """
    MyList class that inherits from list

    """
    def print_sorted(self):
        """
        Function to print the list
        Should be sorted in ascending manner

        """
        print(sorted(self))
