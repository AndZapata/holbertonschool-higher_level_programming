#!/usr/bin/python3

import sys

counter = 0
total_size = 0
status_code = {'200': 0, '301': 0, '400': 0, '401': 0,
               '403': 0, '404': 0, '405': 0, '500': 0}
try:
    for i in sys.stdin:
        stdin_list = i.split(" ")
        code = stdin_list[-2]
        total_size += int(stdin_list[-1])
        if code in status_code.keys():
            status_code[code] = status_code.get(code) + 1
        counter += 1
        if counter % 10 == 0:
            print('File size: {:d}'.format(total_size))
            for key, val in sorted(status_code.items()):
                if val != 0:
                    print('{:s}: {:d}'.format(key, val))
except Exception:
    pass
finally:
    print('File size: {:d}'.format(total_size))
    for key, val in sorted(status_code.items()):
        if val != 0:
            print('{:s}: {:d}'.format(key, val))
