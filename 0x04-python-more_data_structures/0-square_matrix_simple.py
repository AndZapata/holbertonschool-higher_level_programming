#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
    new_matrix = []
    tmp_matrix = []
    for i in matrix:
        for j in i:
            tmp_matrix = list(map(lambda j: j * j, i))
        new_matrix.append(tmp_matrix)
    return new_matrix
