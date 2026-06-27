#!/usr/bin/env python3
"""Dragon module demonstrating mixins."""


class SwimMixin:
    """Mixin for swimming ability."""

    def swim(self):
        """Prints swimming behavior."""
        print("The creature swims!")


class FlyMixin:
    """Mixin for flying ability."""

    def fly(self):
        """Prints flying behavior."""
        print("The creature flies!")


class Dragon(SwimMixin, FlyMixin):
    """Dragon class inheriting from mixins."""

    def roar(self):
        """Prints roaring behavior."""
        print("The dragon roars!")
