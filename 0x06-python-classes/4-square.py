#!/usr/bin/python3
 class Square:
    """Class square"""
    def __init__(self, size=0):
        """Inits class with size."""
        self.__size = size
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")

    def area(self):
        """returns area of square"""
        return self.__size * self.__size

    @property
    def size(self):
        """Getter function to return size."""
        return self.__size

    @size.setter
    def size(self, value):
        """Setter function to set sizee"""
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value
