#!/usr/bin/python3

def print_reversed_list_integer(my_list=[]):
    length = len(my_list)

    i = 1
    while i <= length:
        idx = i * -1
        print("{}".format(my_list[idx]))
        i += 1
