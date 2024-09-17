import pygame
from dataset import *

class Text:

    def __init__(self, text, size, color, bold=False):
        self.font_name = pygame.font.match_font('arial')
        self.font = pygame.font.SysFont('arial', size, bold)
        self.text = text
        self.font_size = self.font.size(text)
        self.color = color
        self.render = self.font.render(self.text, True, color)

    def draw(self, surface, posit):
        surface.blit(self.render, posit)

    def __len__(self):
        return len(self.text)
