#!/usr/bin/python3
def new_in_list(my_list, idx, element):
    x = my_list.copy()
    i = len(x)
    if idx < 0:
        return my_list
    elif idx >= i:
        return my_list
    else:
        x[idx] = element
        return x
