#!/usr/bin/python3
def write_file(filename="", text=""):
    with open(filename, mode='w', encoding='UTF8') as myFile:
        return myFile.write(text)
