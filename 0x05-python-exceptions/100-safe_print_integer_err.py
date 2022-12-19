#!/usr/bin/python3

def safe_print_integer_err(value):
    try:
        print("{:d}".format(value))
        return True
    except (ValueError, TypeError):
        raise Exception("Unknown format code 'd' for object of type 'str'")
        return False
