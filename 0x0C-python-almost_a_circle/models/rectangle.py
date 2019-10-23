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

    if args is not None:
        for i, j in kwargs.items():
                if i == "id":
                    self.id = j
                if i == "width":
                    self.width = j
                if i == "height":
                    self.height = j
                if i == "x":
                    self.x = j
                if i == "y":
                    self.y = j
