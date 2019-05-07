#!/usr/bin/python3
def add_tuple(tuple_a=(), tuple_b=()):
    a = tup_condition(tuple_a)
    b = tup_condition(tuple_b)
    return (a[0] + b[0], a[1] + b[1])

def tup_condition(tup=()):
    l = len(tup)
    if l == 0:
        return ((0, 0))
    elif l == 1:
        tup = list(tup)
        tup.append(0)
        tup = tuple(tup)
    return tup
