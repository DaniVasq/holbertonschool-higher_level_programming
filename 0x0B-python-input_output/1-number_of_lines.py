#!/usr/bin/python3
def number_of_lines(filename=""):
    """function that returns the number of lines in text file."""
    numLines = 0
    with open(filename, encoding="utf8") as f:
        for line in f:
        numLines += 1
    return numLines
