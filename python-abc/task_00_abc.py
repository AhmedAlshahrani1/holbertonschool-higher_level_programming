#!/usr/bin/env python3
"""
Module for Abstract Animal Class and its Subclasses
"""
from abc import ABC, abstractmethod


class Animal(ABC):
    """Abstract class representing an Animal"""

    @abstractmethod
    def sound(self):
        """Abstract method to return the animal's sound"""
        pass


class Dog(Animal):
    """Class representing a Dog"""

    def sound(self):
        """Returns the sound of a dog"""
        return "Bark"


class Cat(Animal):
    """Class representing a Cat"""

    def sound(self):
        """Returns the sound of a cat"""
        return "Meow"
