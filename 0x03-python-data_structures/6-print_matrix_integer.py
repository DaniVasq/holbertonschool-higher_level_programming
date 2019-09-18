#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):
    for x in matrix:
    counter = 0
    for y in x:
        if counter == len(x) - 1:
          print("{:d}".format(y), end=" ")
        else:
         print("{:d}".format(y), end=" ")
        counter += 1
    print()
