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

        """turtle code"""
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

    @staticmethod
    def to_json_string(list_dictionaries):
        """return the JSON representation"""

        if list_dictionaries is None or len(list_dictionaries) == []:
            return "[]"
        return json.dumps(list_dictionaries)

    @classmethod
    def save_to_file(cls, list_objs):
        """JSON str rep of list_objs to file"""

        with open("{}.json".format(cls.__name__), "w",
                      encoding="utf=8") as f:
            if list_objs is None:
                f.write(cls.to_json_string([]))
            else:
                f.write(cls.to_json_string(
                    [(cls.to_dictionary(obj)) for obj in list_objs]))

    @staticmethod
    def from_json_string(json_string):
        """returns list of JSON str rep of json_string"""

        if json_string is None or len(json_string) == []:
            return "[]"
        else:
            return json_string
