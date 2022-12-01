#!/usr/bin/python3
import sys

if __name__ == '__main__':
    argument_length = len(sys.argv)

    sum = 0
    for i in range(1, argument_length):
        sum += int(sys.argv[i])

    print("{:d}".format(sum))
