#!/usr/bin/python3
class Square:
    """class Square"""
    def __init__(self, size=0):
        """init size as zero, an int"""
        self.__size = size
        if not isinstance(size, int):
            """if not of type int, then..."""
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
            """raise exceptions"""
    def size(self):
        """getter to retrieve size"""
        return self.__size
    def size(self, value):
        """setter to set value of size"""
        self.__size = value
    def area(self):
        return self.__size * self.__size
        """returns area of square"""
