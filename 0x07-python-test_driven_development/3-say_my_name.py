#!/usr/bin/python3
""" say_my_name  - Function that prints two strings """


def say_my_name(first_name, last_name=""):
    """
    Raise error message if it is not a type string
    Print two strings
    """
    if type(first_name) != str:
        raise TypeError('first_name must be a string')
    elif type(last_name) != str:
        raise TypeError('last_name must be a string')
    else:
        print("My name is {:s} {:s}".format(first_name, last_name))
