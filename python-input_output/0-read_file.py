#!/usr/bin/python3
"""This module defines a function that reads a text file."""


def read_file(filename=""):

    """Reads a UTF8 text file and prints its content to stdout."""
    with open(filename) as f:
        content = f.read()
        print(content)
