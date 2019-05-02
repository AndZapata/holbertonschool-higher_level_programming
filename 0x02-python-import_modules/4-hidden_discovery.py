#!/usr/bin/python3
import hidden_4
list = dir(hidden_4)
for i in range(len(list)):
    if not (list[i].startswith("__")):
        print(list[i])
