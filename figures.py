import pygame


class BaseFigure(pygame.sprite.Sprite):

    def __init__(self, color, image, cell):
        pygame.sprite.Sprite.__init__(self)
        self.live = 1
        self.image = image
        self.color = color
        self.rect = self.image.get_rect()
        self.rect.center = (cell[0] * 100, cell[1] * 100)

    def attack(self, other):
        pass

    def die(self):
        self.live = 0


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

    def motion(self):
        pass

class Rook(BaseFigure):
    def __init__(self, color, image, cell):
        super().__init__(color, image, cell)

    def castling(self):
        # рокировка
        pass

class Pawn(BaseFigure):
    def __init__(self, color, image, cell):
        super().__init__(color, image, cell)

    def motion(self):
        pass
