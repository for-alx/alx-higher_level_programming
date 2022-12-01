#!/usr/bin/python3
import sys

if __name__ == '__main__':
    length = len(sys.argv)


    if length - 1 == 0:
        print("{} arguments.".format(length - 1))

    else:
        for i in range(1, length):
            if i == 1:
                print("{} arguments:".format(length - 1))

            print("{}: {}".format(i, sys.argv[i]))
