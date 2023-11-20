#!/usr/bin/python3
def safe_print_division(a, b):
    try:
        div = a / b
        print("Inside result: {:.1f}".format(div))
        return div
    except ZeroDivisionError:
        print("Inside result: None")
        return None
