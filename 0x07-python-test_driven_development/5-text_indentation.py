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
    lines = []
    current_line = ""
    for char in text:
        if char in ['.', '?', ':']:
            current_line += char
            lines.append(current_line.strip())
            lines.append("")
            current_line = ""
        else:
            current_line += char
    lines.append(current_line.strip())

    for line in lines:
        print(line)
