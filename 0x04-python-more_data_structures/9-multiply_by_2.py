#!/usr/bin/python3

def multiply_by_2(a_dictionary):
    a_dictionary = {x: x * 2 for k, x in a_dictionary.items()}
    return a_dictionary
