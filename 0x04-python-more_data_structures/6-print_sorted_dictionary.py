#!/usr/bin/python3
def print_sorted_dictionary(a_dictionary):
    a_sorted = dict(sorted(a_dictionary.items()))
    for key in a_sorted.keys():
        print("{}: {}".format(key, a_sorted[key]))
