#!/usr/bin/python3
def read_file(filename=""):
    with open(filename, encoding='UTF8') as myFile:
        for line in myFile:
            print(line, end='')
