#!/usr/bin/python3
def roman_to_int(roman_string):
    if type(roman_string) != str:
        return 0
    dic_rom = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
    total = 0
    for i in range(len(roman_string)):
        chn = dic_rom[roman_string[i]]
        if i + 1 < len(roman_string) and dic_rom[roman_string[i + 1]] > chn:
            total = total - chn
        else:
            total = total + chn
    return total
