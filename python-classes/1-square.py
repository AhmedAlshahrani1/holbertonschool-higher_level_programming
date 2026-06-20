#!/usr/bin/python3
"""
This module defines a Square class.
It introduces private instance attributes and instantiation.
"""


class Square:
    """
    A class that represents a square.
    """
    def __init__(self, size):
        """
        Initializes a new Square instance.

        Args:
            size: The size of the square.
        """
        self.__size = size
