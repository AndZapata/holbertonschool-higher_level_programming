#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
if number < 0:
    mod = ((- 1 * number) % 10) * -1
else:
    mod = number % 10
if mod == 0:
    print("Last digit of {:d} is {:d} and is 0".format(number, mod))
elif mod > 5:
    print("Last digit of {:d} is {:d} and is greater \
than 5".format(number, mod))
elif mod < 6:
    print("Last digit of {: d} is {: d} and is less \
than 6 and not 0".format(number, mod))
