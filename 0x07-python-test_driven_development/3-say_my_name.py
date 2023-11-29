#!/usr/bin/python3
"""
Say_my_name Module
function that prints My name is <first name> <last name>
Prototype: def say_my_name(first_name, last_name=""):

first_name and last_name must be strings otherwise,
raise a TypeError exception with the message first_name must
be a string or last_name must be a string

You are not allowed to import any module

"""


def say_my_name(first_name, last_name=""):
    """
    Function that prints My name is <first name> <last name>


    Args:
        first_name: first name
        last_name: last name

    Raises:
        TypeError: if first_name or last_name is not a string

    """
    fullname = ""
    if first_name and not isinstance(first_name, str):
        raise TypeError('first_name must be a string')
    if last_name and not isinstance(last_name, str):
        raise TypeError('last_name must be a string')
    if first_name:
        fullname += first_name + " "
    if last_name:
        fullname += last_name
    print("My name is {:s}".format(fullname))
