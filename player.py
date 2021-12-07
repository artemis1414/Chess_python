from dataset import figures
from figures import *
from board import board


class Player:
    def __init__(self, color, name):
        self.color = color
        self.name = name
        self.figures = {}
        if self.color == 'white':
            for row in range(6, 8):
                for column in range(0, 8):
                    self.figures[board[row][column]] = ''
        else:
            for row in range(0, 2):
                for column in range(0, 8):
                    self.figures[board[row][column]] = ''

    def act(self):
        pass

    def die(self):
        pass

    def __str__(self):
        return self.name
