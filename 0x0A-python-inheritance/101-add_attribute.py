#!/usr/bin/python3


def add_attribute(obj, name, value):
    if isinstance(obj, (int, bool, float, str, complex, list, tuple, dict,
                        frozenset, set, bytes)):
        raise TypeError('can\'t add new attribute')
    else:
        obj.__setattr__(name, value)
