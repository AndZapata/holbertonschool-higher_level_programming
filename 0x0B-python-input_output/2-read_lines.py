#!/usr/bin/python3
def read_lines(filename="", nb_lines=0):
    with open(filename, encoding='UTF8') as myFile:
        count = 0
        while count < nb_lines or nb_lines <= 0:
            line = myFile.readline()
            if not line:
                break
            count += 1
            print(line, end='')
