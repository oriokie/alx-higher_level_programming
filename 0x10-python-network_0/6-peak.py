#!/usr/bin/python3
"""A function that returns the highest peek in a list of integers"""
def find_peak(list_of_integers):
    """Return the highest peak in a list of integers"""
    size = len(list_of_integers)
    if size == 0:
        return None
    elif size == 1:
        return list_of_integers[0]
    elif size == 2:
        return max(list_of_integers)
    
    """Find the highest peak in the list recursively"""
    mid = size // 2
    left_peak = find_peak(list_of_integers[:mid])
    right_peak = find_peak(list_of_integers[mid:])
    return max(left_peak, right_peak)
