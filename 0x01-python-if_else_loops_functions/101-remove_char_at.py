#!/usr/bin/python3
def remove_char_at(str, n):
    if n < 0:
        return str
    else:
        i = str[:n]
        j = str[n+1:]
        return i + j
