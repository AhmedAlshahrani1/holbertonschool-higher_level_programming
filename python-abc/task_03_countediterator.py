#!/usr/bin/env python3
"""CountedIterator module."""


class CountedIterator:
    """Iterator that tracks the number of iterated items."""

    def __init__(self, iterable):
        """Initializes the iterator and counter."""
        self.iterator = iter(iterable)
        self.counter = 0

    def get_count(self):
        """Returns the current count of iterated items."""
        return self.counter

    def __next__(self):
        """Increments counter and returns the next item."""
        try:
            item = next(self.iterator)
            self.counter += 1
            return item
        except StopIteration:
            raise StopIteration
