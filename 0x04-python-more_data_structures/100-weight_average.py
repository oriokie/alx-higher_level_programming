#!/usr/bin/python3
def weight_average(my_list=[]):
    if my_list == [] or my_list is None:
        return (0)
    t_score = 0
    t_score2 = 0
    for x, y in my_list:
        t_score += x * y
        t_score2 += y
    return (t_score / t_score2)
