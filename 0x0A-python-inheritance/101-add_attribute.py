#!/usr/bin/python3


def add_attribute(obj, name, value):
    if isinstance(obj, (str, int, float, list, tuple,
                        dict, bool, complex)) or obj is None:
        raise TypeError('can\'t add new attribute')
    obj.name = value
