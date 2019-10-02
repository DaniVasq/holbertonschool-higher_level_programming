#!/usr/bin/python3
class Square:
    """a class Square"""
    def __init__(self, size=0):
        """init size with int zero"""
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
    def area(self):
        return self.__size * self.__size
        """returns the area of square"""
