#!/usr/bin/python3
if __name__ == '__main__':
    import sys
    argument_length = len(sys.argv)

# for zero arguments
    if argument_length - 1 == 0:
        print("{} arguments.".format(argument_length - 1))

# for one or more arguments
    else:
        for i in range(1, argument_length):
            if i == 1:
                print("{} arguments:".format(argument_length - 1))

            print("{}: {}".format(i, sys.argv[i]))
