#!/usr/bin/python3
def divisible_by_2(my_list=[]):
    list2 = []
    for i in my_list:
        list2.append(i % 2 == 0)
    return list2
