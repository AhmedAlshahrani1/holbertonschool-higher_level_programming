#!/usr/bin/env python3
"""FlyingFish module demonstrating multiple inheritance."""


class Fish:
    """Fish class."""

    def swim(self):
        """Prints swimming behavior."""
        print("The fish is swimming")

    def habitat(self):
        """Prints fish habitat."""
        print("The fish lives in water")


class Bird:
    """Bird class."""

    def fly(self):
        """Prints flying behavior."""
        print("The bird is flying")

    def habitat(self):
        """Prints bird habitat."""
        print("The bird lives in the sky")


class FlyingFish(Fish, Bird):
    """FlyingFish class inheriting from Fish and Bird."""

    def fly(self):
        """Prints soaring behavior."""
        print("The flying fish is soaring!")

    def swim(self):
        """Prints swimming behavior."""
        print("The flying fish is swimming!")

    def habitat(self):
        """Prints flying fish habitat."""
        print("The flying fish lives both in water and the sky!")
