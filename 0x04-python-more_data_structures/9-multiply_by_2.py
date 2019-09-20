#!/usr/bin/python3
def multiply_by_2(a_dictionary):
    new_one = dict(a_dictionary)
    for x in a_dictionary:
        new_one[x] = new_one[x] * 2
    return new_one
