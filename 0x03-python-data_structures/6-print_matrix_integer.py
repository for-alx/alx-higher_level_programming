#!/usr/bin/python3

def print_matrix_integer(matrix=[[]]):
    if matrix is None:
        print("")

    for i in range(len(matrix)):
        for j in range(len(matrix[i])):
            print("{:d}".format(matrix[i][j]), end=" ")

        print("")
