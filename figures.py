from dataset import pawn


class BaseFigure:

    def __init__(self, x, y):
        self.live = 1
        self.x = x
        self.y = y

    def attack(self, other):
        other.die = 0

    def die(self):
        self.live = 0


class King(BaseFigure):

    def __init__(self, x, y):
        super().__init__(x, y)


    def castling(self):
        # рокировка
        pass


class Queen(BaseFigure):

    def __init__(self, x, y):
        super().__init__(x, y)


class Bishop(BaseFigure):
    def __init__(self, x, y):

        super().__init__(x, y)


class Knight(BaseFigure):
    def __init__(self, x, y):
        super().__init__(x, y)

    def motion(self):
        pass

class Rook(BaseFigure):
    def __init__(self, x, y):
        super().__init__(x, y)

    def castling(self):
        # рокировка
        pass

class Pawn(BaseFigure):
    def __init__(self, x, y):
        super().__init__(x, y)
        self.act = 0

    def motion(self):
        pass
