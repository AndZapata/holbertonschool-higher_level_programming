#!/usr/bin/python3
"""  """


class Rectangle:
    number_of_instances = 0

    def __init__(self, width=0, height=0):
        self.width = width
        self.height = height
        Rectangle.number_of_instances += 1

    @property
    def width(self):
        return self.__width

    @width.setter
    def width(self, value):
        if type(value) != int:
            raise TypeError('width must be an integer')
        elif value < 0:
            raise ValueError('width must be >= 0')
        else:
            self.__width = value

    @property
    def height(self):
        return self.__height

    @height.setter
    def height(self, value):
        if type(value) != int:
            raise TypeError('height must be an integer')
        elif value < 0:
            raise ValueError('height must be >= 0')
        else:
            self.__height = value

    def area(self):
        return self.width * self.height

    def perimeter(self):
        if self.width == 0 and self.height == 0:
            return 0
        return (self.width * 2) + (self.height * 2)

    def __str__(self):
        if self.width == 0 or self.height == 0:
            return ''
        list1 = []
        for i in range(self.height):
            list1.append('#' * self.width)
            if i < (self.height - 1):
                list1.append('\n')
        return ''.join(list1)

    def __repr__(self):
        return 'Rectangle({:d}, {:d})'.format(self.width, self.height)

    def __del__(self):
        print('Bye rectangle...')
        Rectangle.number_of_instances -= 1
