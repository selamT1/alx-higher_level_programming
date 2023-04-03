#!/usr/bin/python3
""" Define a class rectangle"""


class Rectangle:
    """ a class to rectangle"""
    def __init__(self, width=0, height=0):
        """ initialization of the rectangle
        Parameters
        -----------
        width: int
            width of the rectangle
        height: int
            height of the rectangle
        """
        self.width = width
        self.height = height

    @property
    def width(self):
        """ get width of rectangle"""
        return (self.__width)

    @width.setter
    def width(self, value):
        """set width of rectangle"""
        if not isinstance(value, int):
            raise TypeError('width must be an integer')
        elif value < 0:
            raise valueError('width must be >= 0')
        else:
            self.__width = value

    @property
    def height(self):
        """ get height of rectangle"""
        return (self.__height)

    @height.setter
    def height(self, value):
        """set height of rectangle"""
        if not isinstance(value, int):
            raise TypeError('height must be an integer')
        elif value < 0:
            raise valueError('height must be >= 0')
        else:
            self.__height = value
