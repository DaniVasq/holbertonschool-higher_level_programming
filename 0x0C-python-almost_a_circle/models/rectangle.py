#!/usr/bin/python3
"""class Rectangle that inherits from Base"""


from models.base import Base


class Rectangle(Base):
    """Rectangle class based on Base"""

    def __init__(self, width, height, x=0, y=0, id=None):
        """private attributes"""

        self.width = width
        self.height = height
        self.x = x
        self.y = y
        super().__init__(id)

    @property
    def width(self):
        """getter for width"""
        return self.__width

    @width.setter
    def width(self, value):
        """setter"""

        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        elif value <= 0:
            raise ValueError("width must be > 0")
        else:
            self.__width = value

    @property
    def height(self):
        """getter height"""

        return self.__height

    @height.setter
    def height(self, value):
        """setter height"""

        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        elif value <= 0:
            raise ValueError("height must be > 0")
        else:
            self.__height = value

    @property
    def x(self):
        """getter for x"""

        return self.__x

    @x.setter
    def x(self, value):
        """setter for x"""

        if not isinstance(value, int):
            raise TypeError("x must be an integer")
        elif value < 0:
            raise ValueError("x must be >= 0")
        else:
            self.__x = value

    @property
    def y(self):
        """getter for y"""

        return self.__y

    @y.setter
    def y(self, value):
        """setter for y"""

        if not isinstance(value, int):
            raise TypeError("y must be an integer")
        elif value < 0:
            raise ValueError("y must be >= 0")
        else:
            self.__y = value

    def area(self):
        """returns the area of rectangle"""

        return self.width * self.height

    def display(self):
        """prints # in a rectangle"""

        for i in range(self.__y):
            print()
        for j in range(self.__height):
            print(" " * self.__x, end="")
            for c in range(self.__width):
                print("#", end="")
            print()

    def __str__(self):
        """str function to print"""

        return "[Rectangle] ({}) {}/{} - {}/{}".format(self.id, self.x,
                                                       self.y, self.width,
                                                       self.height)

    def update(self, *args, **kwargs):
        """assigns arg to each attribute"""

        if args is not None and len(args) != 0:
            for i, j in enumerate(args):
                if i == 0:
                    self.id = j
                if i == 1:
                    self.width = j
                if i == 2:
                    self.height = j
                if i == 3:
                    self.x = j
                if i == 4:
                    self.y = j
        else:
            for c, j in kwargs.items():
                setattr(self, c, j)

    def to_dictionary(self):
        """dictionary representationp"""

        my_dict = {}
        my_dict["id"] = self.id
        my_dict["size"] = self.size
        my_dict["x"] = self.x
        my_dict["y"] = self.y
        return my_dict
