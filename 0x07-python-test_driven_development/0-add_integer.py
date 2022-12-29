#!/usr/bin/python3
"""
    This module calculate the sum of two numbers
    with argument parameter control
"""


def add_integer(a, b=98):
    """
    This function return the addition of two numbers
    a and b must be integers or floats
    otherwise raise a TypeError exception with the message
    'a must be an integer' or 'b must be an integer'

    Args:
        a (int):
        b (int):
    Returns:
        int: return addition of two numbers without decimal point
    """
    if type(a) != float and type(a) != int:
        raise TypeError('a must be an integer')
    if type(b) != float and type(b) != int:
        raise TypeError('b must be an integer')

    return int(a) + int(b)
