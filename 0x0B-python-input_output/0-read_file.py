#!/usr/bin/python3
def read_file(filename=""):
"""function that reads a text file(UTF8) and prints to stdout."""
    with open(filename, encoding="utf8" ) as f:
        print(f.read(),end="")
