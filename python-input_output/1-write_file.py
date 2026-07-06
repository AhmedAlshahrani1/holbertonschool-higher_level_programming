#!/usr/bin/python3
"""This module defines a function that writes a string to a text file."""


def write_file(filename="", text=""):


    """Writes a string to a UTF8 text file and returns
    the number of characters written."""

    with open(filename, "w") as f:
        return f.write(text)
