#!/usr/bin/python3
"""This module defines a function that appends a string to a text file."""


def append_write(filename="", text=""):
    """Appends a string at the end of a UTF8 text file and returns
    the number of characters added."""
    with open(filename, "a") as f:
        return f.write(text)
