#!/usr/bin/python3
def only_diff_elements(set_1, set_2):
    el_1 = [i for i in set_1 if i not in set_2]
    el_2 = [i for i in set_2 if i not in set_1]
    return el_1 + el_2
