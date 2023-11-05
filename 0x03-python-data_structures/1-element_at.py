#!/usr/bin/python3
def element_at(my_list, idx):
    size = len(my_list) - 1
    if idx < 0 or idx > size:
        return None
    else:
        return my_list[idx]
