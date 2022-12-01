#!/usr/bin/python3
from sys import argv

if __name__ == '__main__':
    length = len(argv)

    if length - 1 == 0:
        print("{} arguments.".format(length - 1))
    else:
        for i in range(1, length):
            if i == 1:
                print("{} arguments:".format(length - 1))

            print("{}: {}".format(i, argv[i]))
