#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):
    for row in matrix:
        count = 0
        for elem in row:
            if len(row) - 1 > count:
                print("{:d}".format(elem), end=' ')
            else:
                print("{:d}".format(elem), end='')
            count += 1
        print()
