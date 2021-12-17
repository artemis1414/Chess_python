from dataset import figures
from figures import *
from board import board
import pygame

class Player:
    def __init__(self, x, y, w, h, color, name):
        self.bounds = pygame.rect.Rect(x, y, w, h)
        self.color = color
        self.name = name
        self.screen_white_game = {}

    def act(self):
        pass

    def die(self):
        pass

    def __str__(self):
        return self.name
