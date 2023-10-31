#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
sign = 1
if number < 0:
    sign = -1
last_digit = (abs(number) % 10) * sign

if last_digit > 5:
    close = " and is greater than 5"
elif last_digit < 6 and last_digit and not 0:
    close = " and is less than 6 and not 0"
else:
    close = " and is 0"
print("Last digit of {0:d} is {1:d}{2}".format(number, last_digit, close))
