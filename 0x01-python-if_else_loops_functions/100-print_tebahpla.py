#!/usr/bin/python3
for letter in range(122, 96, -1):
    if letter % 2 == 1:
        letter -= 32
    print("{}".format(chr(letter)), end="")
