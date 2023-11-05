#!/usr/bin/python3
def no_c(my_string):
    size = len(my_string) - 1
    new_string = []
    idx = 0
    if idx < 0 or idx > size:
        return my_string
    else:
        for item in my_string:
            if item != "c" and item != "C":
                new_string.append(item)
    return ''.join(new_string)
