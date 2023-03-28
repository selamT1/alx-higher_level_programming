#!/usr/bin/python3
"""Define a class Square."""


class Square():
    """ a class to squares """
    def __init__(self, size=0):
        """ initialization to the new square.
        Parameters
        --------------
        size: int
            the size of the square
        """
        self.size = size

    @property
    def size(self):
        """get size of square"""
        return (self.__size)

    @size.setter
    def size(self, value):
        """set size of square"""
        if not isinstance(value, int):
            raise TypeError('size must be an integer')
        elif value < 0:
            raise ValueError('size must be >= 0')
        else:
            self.__size = value

    def area(self):
        """Return area of the square"""
        return (self.__size * self.__size)
