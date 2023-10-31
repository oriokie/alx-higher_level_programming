#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
last_digit = abs(number) % 10
if last_digit > 5:
    close = "greater than 5"
elif last_digit < 6 and last_digit and not 0:
    close = "less than 6 and not 0"
else:
    close = "0"
print("Last digit of {0:d} is {1:d} and is {2}".format(number, last_digit, close))
