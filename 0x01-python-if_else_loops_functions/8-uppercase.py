#!/usr/bin/python3
def uppercase(str):
    x = 0
    while x < len(str):
        if str[x].islower():
            y = ord(str[x]) - 32
        else:
            y = ord(str[x])
        if x != len(str):
            print("{:s}".format(chr(y)), end="")
        x += 1
    print("")
