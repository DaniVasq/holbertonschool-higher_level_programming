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

    def update(self, *args, **kwargs)
        """assigns attributes"""

        if args is not None and len(args) != 0:
            for i, j in enumerate(args):
                if i == 0:
                    self.id = j
                if i == 1:
                    self.size = j
                if i == 2:
                    self.x = j
                if i == 3:
                    self.y = j
        else:
            for k, v in kwargs.items():
                setattr(self, c, j)
