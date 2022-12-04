#!/usr/bin/python3
print_matrix_integer = __import__('6-print_matrix_integer').print_matrix_integer

matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

print_matrix_integer(matrix)
print("--")
print_matrix_integer()


# Rlength = len(matrix)
# Clength = len(matrix[0])

# print(Rlength)
# print(Clength)

# for i in range(len(matrix)):

# 	# print(matrix[i])
# 	for j in range(len(matrix[i])):
# 		print(matrix[i][j], end="")
# 	print()
