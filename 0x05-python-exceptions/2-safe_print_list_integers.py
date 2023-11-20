#!/usr/bin/python3
def safe_print_list_integers(my_list=[], x=0):
    counter = 0
    try:
        for number in range(x):
            print("{:d}".format(my_list[number]), end='')
            counter += 1
    except (ValueError, IndexError, TypeError):
        pass
    print()
    return counter
