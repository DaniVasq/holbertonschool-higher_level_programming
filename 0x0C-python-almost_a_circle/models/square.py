#!/usr/bin/python3
"""Square class module"""
from models.rectangle import Rectangle


class Square(Rectangle):
    """class Square inheriting from Rectangle class"""

    def __init__(self, size, x=0, y=0, id=None):
        """instantiation of class Square"""

        super().__init__(size, size, x, y, id)

    def __str__(self):
        """str method that returns output"""

        return ("[Square] ({}) {}/{} - {}".format(
            self.id, self.x, self.y, self.width))

    @property
    def size(self):
        """getter for size"""

        return self.width

    @size.setter
    def size(self, value):
        """setter for size"""

        self.width = value
        self.height = value
