#!/usr/bin/python3
class Square:
    """class Square"""
    def __init__(self, size=0):
        self.__size = size

    @property
    def size(self):
        """function to get size"""
        return self.__size

    @size.setter
    def size(self, value):
        """function to set size value"""
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    def area(self):
        return self.__size * self.__size

    def my_print(self):
        """function to print the square in #"""
        if self.__size == 0:
            print()
        else:
            for x in range(self.__size):
                    for i in range(self.__size):
                        print("#", end="")
                    print()
