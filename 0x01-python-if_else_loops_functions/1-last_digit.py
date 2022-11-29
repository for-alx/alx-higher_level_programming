#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)

last_num = int(repr(number)[-1])

if number > 0:
    if last_num > 5:
        print("Last digit of {:d} is {:d} and is greater than 5".format(number, last_num))
    elif last_num == 0:
        print("Last digit of {:d} is {:d} and is 0".format(number, last_num))
    elif last_num < 6:
        print("Last digit of {:d} is {:d} and is less than 6 and not 0".format(number, last_num))
else:
    if last_num < 5:
        print("Last digit of {:d} is {:d} and is greater than 5".format(number, last_num * -1))
    elif last_num == 0:
        print("Last digit of {:d} is {:d} and is 0".format(number, last_num * -1))
    elif last_num > 6:
        print("Last digit of {:d} is {:d} and is less than 6 and not 0".format(number, last_num * -1))