#!/usr/bin/python3
def pascal_triangle(n):
    if n <= 0:
        return []
    list1 = [[1], [1, 1]]
    for i in range(1, n - 1):
        line = [1]
        for j in range(0, len(list1[i]) - 1):
            line.extend([list1[i][j] + list1[i][j + 1]])
        list1.append(line)
        line += [1]
    return list1
