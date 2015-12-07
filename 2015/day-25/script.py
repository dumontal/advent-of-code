#!/usr/bin/env python

def find_code(row, col):
    i, j, code = 1, 1, 20151125

    while not (i == row and j == col):
        i, j = (i - 1, j + 1) if i > 1 else (j + 1, 1)
        code = (code * 252533) % 33554393

    return code

if __name__ == '__main__':
    print('[Part 1] Code is:', find_code(2978, 3083))
