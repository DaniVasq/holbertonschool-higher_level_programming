#!/usr/bin/python3
class Square:
    """class Square"""
    def __init__(self, size=0):
        """init size as zero, an int"""
        self.__size = size
    @property
    def size(self):
        """getter to retrieve size"""
        return self.__size
    @size.setter
    def size(self, value):
        """setter to set value of size"""
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value
    def area(self):
        return self.__size * self.__size
        """returns area of square"""
