#!/usr/bin/python3
def multiply_by_2(a_dictionary):
    values = list(map(lambda x: x * 2, a_dictionary.values()))
    keys = a_dictionary.keys()
    return (dict(zip(keys, values)))
