#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):
    for x in matrix:
        count = 0
        for i in row:
            if len(x) - 1 > count:
                print("{:d}".format(i), end=' ')
            else:
                print("{:d}".format(i), end='')
            count += 1
        print()
