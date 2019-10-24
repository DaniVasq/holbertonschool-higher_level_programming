#!/usr/bin/python3
"""Base class module"""


class Base:
    """Base class"""
    __nb_objects = 0

    def __init__(self, id=None):
        """instantiation of base"""
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

@staticmethod
    def draw(list_rectangles, list_squares):
        dani = turtle.Turtle()
        dani.shape("turtle")
        dani.color("Dark Salmon")
        for r in list_rectangles:
            dani.showturtle()
            dani.up()
            dani.goto(r.x, r.y)
            dani.down()
            for i in range(2):
                dani.forward(r.width)
                dani.left(90)
                dani.forward(r.height)
                dani.left(90)
            dani.hideturtle()
        dani.color("Medium Aquamarine")
        for s in list_squares:
            dani.showturtle()
            dani.up()
            dani.goto(s.x, s.y)
            dani.down()
            for i in range(2):
                dani.forward(s.width)
                dani.left(90)
                dani.forward(s.width)
                dani.left(90)
            dani.hideturtle()
        dani.done()
