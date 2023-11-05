#!/usr/bin/python3
def new_in_list(my_list, idx, element):
    temp = my_list.copy()
    size = len(temp) - 1
    if idx < 0 or idx > size:
        return my_list
    else:
        temp[idx] = element
        return temp
