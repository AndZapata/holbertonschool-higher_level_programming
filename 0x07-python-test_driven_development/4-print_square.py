#!/usr/bin/python3
""" print_square - Print a square with a especial character # """


def print_square(size):
    """
    Recieved parameters size as the lenght of a square
    first conditional raise an error if the size are not type integers
    Second conditional raise an error message if size is < than 0
    Finally:
    print the square
    """
    if type(size) != int:
        raise TypeError('size must be an integer')
    elif size < 0:
        raise ValueError('size must be >= 0')
    else:
        for i in range(size):
            for i in range(size):
                print("{}".format('#'), end='')
            print()
