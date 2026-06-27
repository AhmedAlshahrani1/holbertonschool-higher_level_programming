#!/usr/bin/env python3
"""VerboseList module."""


class VerboseList(list):
    """Custom list that prints notifications."""

    def append(self, item):
        """Appends an item to the list."""
        super().append(item)
        print(f"Added [{item}] to the list.")

    def extend(self, iterable):
        """Extends the list with an iterable."""
        count = len(iterable)
        super().extend(iterable)
        print(f"Extended the list with [{count}] items.")

    def remove(self, item):
        """Removes an item from the list."""
        print(f"Removed [{item}] from the list.")
        super().remove(item)

    def pop(self, index=-1):
        """Pops an item from the list."""
        item = self[index]
        print(f"Popped [{item}] from the list.")
        return super().pop(index)
