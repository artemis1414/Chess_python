from dataset import figures
from figures import *
from board import board


class Player:
    def __init__(self, color, name):
        self.color = color
        self.name = name
        self.figures = {}

    def act(self):
        pass

    def die(self):
        pass

    def __str__(self):
        return self.name
