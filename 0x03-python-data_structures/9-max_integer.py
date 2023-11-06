#!/usr/bin/python3
def max_integer(my_list=[]):
    i = 0
    if not my_list:
        return None
    else:
        for item in my_list:
            if item > i:
                i = item
            else:
                continue
    return i
