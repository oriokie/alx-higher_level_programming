#!/usr/bin/python3
"""
Text identation module

"""


def text_indentation(text):
    """
    Function that prints a text with 2 new lines after
    each of these characters: ., ? and :
    text must be a string

    There should be no space at the beginning or
    at the end of each printed line

    Args:
        text: string

    Raises:
        TypeError: if text is not a string

    """
    if type(text) is not str:
        raise TypeError("text must be a string")
    for char in ".?:":
        text = text.replace(char, char + "\n\n")
    lines = [line.strip() for line in text.splitlines()]
    print("\n".join(lines))
