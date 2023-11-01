#!/usr/bin/python3
def print_last_digit(number):
    sign = 1
    if number < 0:
        sign = -1
    last_digit = (sign *number) % 10
    print("{}".format(last_digit), end='')
    return last_digit
