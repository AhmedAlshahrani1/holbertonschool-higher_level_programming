#!/usr/bin/python3


class Student:
    def __init__(self, score=0):
        self.score = score
    @property
    def score(self):
        return self.__score
    @score.setter
    def score(self, score):
        if type(score) != int:
            raise TypeError("score must be an integer")
        if score < 0 or score > 100:
            raise ValueError("score must be between 0 and 100")
        self.__score = score

