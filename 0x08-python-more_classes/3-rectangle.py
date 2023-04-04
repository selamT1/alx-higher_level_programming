#!/usr/bin/python3
"""Define a class Rectangle."""


class Rectangle:
    """a class to Rectangle"""
    def __init__(self, width=0, height=0):
        """ initialization of the rectangle
        Parameters
        -----------
        width: int
            width of the rectangle
        height: int
            height of the rectangle
        """
        self.height = height
        self.width = width

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

    def area(self):
        """ Return area of the rectangle"""
        return (self.__height * self.__width)

    def perimeter(self):
        """Return perimeter of the rectangle"""
        if self.__height == 0 and self.__width == 0:
            return (0)
        else:
            return ((2 * self.__height) + (2 * self.__width))

    def __str__(self):
        """print a Rectangle with '#'"""
        return '\n'.join('#' * self.__width for _ in range(self.__height))
