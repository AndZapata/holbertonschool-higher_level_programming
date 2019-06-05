#!/usr/bin/python3
from sys import argv
load_from_json_file = __import__('8-load_from_json_file').load_from_json_file
save_to_json_file = __import__('7-save_to_json_file').save_to_json_file

list1 = []

try:
    read_f = load_from_json_file("add_item.json")
    for x in read_f:
        list1.append(x)
except:
    pass
for x in range(len(argv)):
    if x > 0:
        list1.append(argv[x])

save_to_json_file(list1, "add_item.json")
