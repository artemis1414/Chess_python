import pygame


class BaseFigure(pygame.sprite.Sprite):

    def __init__(self, color, image, cell):
        pygame.sprite.Sprite.__init__(self)
        self.image = image
        self.color = color
        self.rect = self.image.get_rect()
        self.rect.center = (cell[0] * 100, cell[1] * 100)
        self.focus = False
 
    def attack(self, other):
        other.kill()

    def handle_mouse_down(self):
        self.focus = True

    def motion(self, pos):
        if self.rect.collidepoint(pos):
            self.handle_mouse_down()
            self.rect = self.image.get_rect()
        else:
            self.focus = False

    def update(self):
        self.rect = self.image.get_rect()


class King(BaseFigure):

    def __init__(self, color, image, cell):
        super().__init__(color, image, cell)

    def castling(self):
        # рокировка
        pass


class Queen(BaseFigure):

    def __init__(self, color, image, cell):
        super().__init__(color, image, cell)


class Bishop(BaseFigure):
    def __init__(self, color, image, cell):
        super().__init__(color, image, cell)


class Knight(BaseFigure):
    def __init__(self, color, image, cell):
        super().__init__(color, image, cell)



class Rook(BaseFigure):
    def __init__(self, color, image, cell):
        super().__init__(color, image, cell)

    def castling(self):
        # рокировка
        pass

class Pawn(BaseFigure):
    def __init__(self, color, image, cell):
        super().__init__(color, image, cell)

