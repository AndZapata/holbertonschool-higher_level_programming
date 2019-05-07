#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):
    for row in range(len(matrix)):
        for elm in range(len(matrix[row])):
            if elm < len(matrix[row]) - 1:
                print("{:d}".format(matrix[row][elm]), end=' ')
            else:
                print("{:d}".format(matrix[row][elm]), end='')
        print("")
