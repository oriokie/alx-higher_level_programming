#!/usr/bin/python3
def safe_function(fct, *args):
    import sys
    try:
        return fct(*args)
    except Exception as Err:
        print("Exception: {}".format(Err), file=sys.stderr)
