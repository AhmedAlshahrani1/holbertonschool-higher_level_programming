#!/usr/bin/python3
"""Module for BaseGeometry class."""


class BaseGeometry:
    """A class representing base geometry."""

    def area(self):
        """Raises an exception indicating area is not implemented."""
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """Validates if a value is an integer strictly greater than 0."""
        if type(value) is not int:
            raise TypeError("{} must be an integer".format(name))
        if value <= 0:
            raise ValueError("{} must be greater than 0".format(name))
