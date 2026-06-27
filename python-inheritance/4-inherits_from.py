#!/usr/bin/python3
"""Module to check if an object is a strict subclass instance."""


def inherits_from(obj, a_class):
    """Returns True if obj is strictly an instance of a subclass of a_class."""
    return isinstance(obj, a_class) and type(obj) is not a_class
