#!/usr/bin/python3
if __name__ == "__main__":
    import sys
    arguments = sys.argv
    i = len(arguments) - 1

    if i == 0:
        print("{} arguments.".format(i))
    elif i == 1:
        print("{} argument:".format(i))
    else:
        print("{} arguments:".format(i))

    if i >= 1:
        for arg in range(1, i + 1):
            print("{}: {}".format(arg, arguments[arg]))
