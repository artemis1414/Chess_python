import pygame
from dataset import *


class Cell(pygame.sprite.Sprite):
    def __init__(self, color, cell):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.Surface((100, 100))
        if color == "white":
            self.image.fill(WHITE)
        else:
            self.image.fill(GREY)
        self.rect = self.image.get_rect()
        self.rect.center = (cell[0] * 100, cell[1] * 100)



