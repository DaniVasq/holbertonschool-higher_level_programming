#!/usr/bin/python3
class Square:
    """Class square"""
    def __init__(self, size=0, position=(0, 0)):
        """Inits class size/position"""
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size

        if (isinstance(position, tuple) and
                len(position) == 2 and isinstance(position[0], int) and
                isinstance(position[1], int) and
                position[0] >= 0 and position[1] >= 0):
            self.__position = position
        else:
            raise TypeError("position must be a tuple of 2 positive integers")

    def area(self):
        """returns area of square"""
        return self.__size * self.__size

    @property
    def size(self):
        """Return size value"""
        return self.__size

    @size.setter
    def size(self, value):
        """Setter function to set size"""
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    def my_print(self):
        """Prints square to stdout with #"""
        value = self.__position
        col, row = value[0], value[1]
        if self.__size == 0:
            print()
        for i in range(0, row):
            print()
        for j in range(0, self.__size):
            print(" " * col + '#' * self.__size)

    @property
    def position(self):
        """Returns position"""
        return self.__position

    @position.setter
    def position(self, value):
        """Sets position"""
        if (isinstance(position, tuple) and
                len(position) == 2 and isinstance(position[0], int) and
                isinstance(position[1], int) and
                position[0] >= 0 and position[1] >= 0):
            self.__position = value
        else:
            raise TypeError("position must be a tuple of 2 positive integers")
