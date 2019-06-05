#!/usr/bin/python3
def number_of_lines(filename=""):
    with open(filename, encoding='UTF8') as myFile:
        count = 0
        while True:
            line = myFile.readline()
            if not line:
                break
            count += 1
        return count
