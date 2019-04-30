#!/usr/bin/python3
def uppercase(str):
    if str == '':
        return(ord(str))
    x = 0
    while x < len(str):
        if str[x].islower():
            y = ord(str[x]) - 32
        else:
            y = ord(str[x])
        if x != len(str) - 1:
            print("{:s}".format(chr(y)), end="")
        else:
            print("{:s}".format(chr(y)))
        x += 1
