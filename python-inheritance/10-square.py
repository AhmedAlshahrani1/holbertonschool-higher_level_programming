#!/usr/bin/python3
"""Module for Square class that inherits from Rectangle."""
Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """A class representing a square, inheriting from Rectangle."""

    def __init__(self, size):
        """Initializes a new Square with a private size."""
        self.integer_validator("size", size)
        self.__size = size
        super().__init__(size, size)
