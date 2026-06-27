#!/usr/bin/python3
"""Module to check if an object is an instance of a class or subclass."""


def is_kind_of_class(obj, a_class):
    """Returns True if obj is an instance or inherited instance of a_class."""
    return isinstance(obj, a_class)
