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

    def update(self, *args, **kwargs):
        """update method"""
        j = 0
        if isinstance(args, tuple) and len(args) > 0:
            for arg in args:
                if j == 0:
                    self.id = arg
                if j == 1:
                    self.size = arg
                if j == 2:
                    self.x = arg
                if j == 3:
                    self.y = arg
                j += 1
        for k, v in kwargs.items():
            if k == "id":
                self.id = v
            if k == "size":
                self.size = v
            if k == "x":
                self.x = v
            if k == "y":
                self.y = v

    def to_dictionary(self):
        """return the dict representation of a square"""
        my_dict = {}
        my_dict["id"] = self.id
        my_dict["size"] = self.size
        my_dict["x"] = self.x
        my_dict["y"] = self.y
        return my_dict
