#!/usr/bin/python3
def print_sorted_dictionary(a_dictionary):
    sorted(a_dictionary.key())
    for elem in sorted(a_dictionary.item()):
        print(elem[0], "::", elem[1])
