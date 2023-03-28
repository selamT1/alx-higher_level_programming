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
        if not isinstance(size, int):
            raise TypeError('size must be an integer')
        elif size < 0:
            raise ValueError('size must be >= 0')
        else:
            self.__size = size

    def area(self):
        """Return area of the square"""
        return (self.__size * self.__size)
