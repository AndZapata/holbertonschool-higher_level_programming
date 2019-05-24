#!/usr/bin/python3
""" matrix-divided - Function that divide a matrix into an integer """


def matrix_divided(matrix, div):
    """
    check the matrix for every type it recieves if it is a int or float
    check the div for every type it recieves if it is a int or float
    check for the number that recieves the div if is 0 raise error message
    check for the longitud of the matrix
    return a new matrix with the operation
    retrun matrix / div
    """
    new_mat = []
    tmp_mat = []
    err = "Each row of the matrix must have the same size"
    err_mes = "matrix must be a matrix (list of lists) of integers/floats"
    if  type(div) != int and type(div) != float:
        raise TypeError('div must be a number')
    elif div == 0:
        raise ZeroDivisionError('division by zero')
    else:
        lon = len(matrix[0])
        for i in matrix:
            if lon != len(i):
                raise TypeError(err)
            for j in i:
                if type(j) != int and type(j) != float:
                    raise TypeError(err_mes)
                tmp_mat = list(map(lambda j: round((j / div), 2), i))
            new_mat.append(tmp_mat)
        return new_mat
