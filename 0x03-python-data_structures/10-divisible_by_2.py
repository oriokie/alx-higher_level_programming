#!/usr/bin/python3
def divisible_by_2(my_list=[]):
    if not my_list:
        return None
    len_list = len(my_list) - 1
    i = 0
    new_list=[]
    while i < len_list:
        if my_list[i] % 2 == 0:
            new_list.append(True)
        else:
            new_list.append(False)
        i += 1
    return new_list
