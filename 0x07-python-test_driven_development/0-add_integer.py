#!/usr/bin/python3
""" add_integer - function that adds two integers or floats"""


def add_integer(a, b=98):
    """
    Recieved parameters a and b
    first conditional test if a is not an integer or a float
    second conditional test if b is not an integer or a float
    finally
    Returns a + b
    """
    if type(a) != int and type(a) != float:
        raise TypeError('a must be an integer')
    elif type(b) != int and type(b) != float:
        raise TypeError('b must be an integer')
    else:
        if abs(a + b) == float('inf'):
            raise OverflowError('overflow error')
        return (int(a) + int(b))
