#!/usr/bin/python3
""" Module Square.py """
from models.rectangle import Rectangle


class Square(Rectangle):
    """ Class Square that inheritance from Rectangle """

    def __init__(self, size, x=0, y=0, id=None):
        """ Initialization """
        super().__init__(size, size, x, y, id)

    def __str__(self):
        """ Magic function __str__ prints a representation """
        return ('[Square] ({}) {}/{} - {}'
                .format(self.id, self.x, self.y, self.width))

    @property
    def size(self):
        """ Function that returns the size of the square """
        return super().width

    @size.setter
    def size(self, value):
        """ Function that recognize the size of a square """
        super(Square, self.__class__).width.fset(self, value)
        super(Square, self.__class__).height.fset(self, value)

    def update(self, *args, **kwargs):
        """ Function to update the values for a dictionary """
        list_args = ['id', 'size', 'x', 'y']
        if args:
            for i in range(len(args)):
                setattr(self, list_args[i], args[i])
        else:
            for key, val in kwargs.items():
                setattr(self, key, val)

    def to_dictionary(self):
        """ Function that returns a dictionary """
        return ({'id': self.id, 'size': self.width, 'x': self.x, 'y': self.y})
