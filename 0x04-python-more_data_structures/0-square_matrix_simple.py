#!/usr//bin/python3

def square_matrix_simple(matrix=[]):
    result = []
    for row in matrix:
        temp = []
        k = 0
        for item in row:
            temp.append(item ** 2)
            k += 1
        result.append(temp)
    return result
