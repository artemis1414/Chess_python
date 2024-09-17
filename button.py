import pygame
import dataset

class Button:

    def __init__(self, x, y, w, h, text, on_click=lambda x: None):
        self.bounds = pygame.rect.Rect(x, y, w, h)
        self.text = text
        self.x = x
        self.y = y
        self.background_color = dataset.WHITE
        self.on_click = on_click

    def draw(self, surface):
        text_size_x, text_size_y = self.text.font_size
        posit = (self.bounds.left - text_size_x // 2 + self.bounds.w // 2, self.bounds.top - text_size_y // 2 + self.bounds.h // 2)
        pygame.draw.rect(surface=surface, color=self.background_color, rect=self.bounds)
        self.text.draw(surface, posit)

    def handle_mouse_up(self, pos):
        if self.bounds.collidepoint(pos):
            self.on_click()






