#!/usr/bin/python3
''' function that finds a peak in a list of unsorted integers '''


def find_peak(list_of_integers):
    ''' finds a peak in a list of unsorted integers '''
    if len(list_of_integers) == 0:
        return None
    if len(list_of_integers) == 1:
        return 0
    return list_of_integers[find_peak_recursive(list_of_integers,
                                                0, len(list_of_integers) - 1)]


def find_peak_recursive(ls_int, low, hight):
    ''' Function to select the peak recursively '''
    gap = hight - low
    if gap == 1:
        if ls_int[low] > ls_int[hight]:
            return low
        else:
            return hight
    mid = low + gap // 2
    if ls_int[mid] < ls_int[mid + 1]:
        return find_peak_recursive(ls_int, mid, hight)
    return find_peak_recursive(ls_int, low, mid)
