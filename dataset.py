import os
import figures
import pygame
from button import Button
from text import Text

WIDTH = 1500
HEIGHT = 900
FPS = 60

game_folder = os.path.dirname(__file__)
img_folder = os.path.join(game_folder, 'image_png')
pygame.font.init()


start_position_black = {
 (1, 8): figures.Rook, (2, 8): figures.Knight, (3, 8): figures.Bishop, (4, 8): figures.King, (5, 8): figures.Queen, (6, 8): figures.Bishop, (7, 8): figures.Knight, (8, 8): figures.Rook,
 (1, 7): figures.Pawn, (2, 7): figures.Pawn, (3, 7): figures.Pawn, (4, 7): figures.Pawn, (5, 7): figures.Pawn, (6, 7): figures.Pawn, (7, 7): figures.Pawn, (8, 7): figures.Pawn,
 (1, 6): None, (2, 6): None, (3, 6): None, (4, 6): None, (5, 6): None, (6, 6): None, (7, 6): None, (8, 6): None,
 (1, 5): None, (2, 5): None, (3, 5): None, (4, 5): None, (5, 5): None, (6, 5): None, (7, 5): None, (8, 5): None,
 (1, 4): None, (2, 4): None, (3, 4): None, (4, 4): None, (5, 4): None, (6, 4): None, (7, 4): None, (8, 4): None,
 (1, 3): None, (2, 3): None, (3, 3): None, (4, 3): None, (5, 3): None, (6, 3): None, (7, 3): None, (8, 3): None,
 (1, 2): figures.Pawn, (2, 2): figures.Pawn, (3, 2): figures.Pawn, (4, 2): figures.Pawn, (5, 2): figures.Pawn, (6, 2): figures.Pawn, (7, 2): figures.Pawn, (8, 2): figures.Pawn,
 (1, 1): figures.Rook, (2, 1): figures.Knight, (3, 1): figures.Bishop, (4, 1): figures.King, (5, 1): figures.Queen, (6, 1): figures.Bishop, (7, 1): figures.Knight, (8, 1): figures.Rook,
}
start_position_white = {
 (1, 8): figures.Rook, (2, 8): figures.Knight, (3, 8): figures.Bishop, (4, 8): figures.Queen, (5, 8): figures.King, (6, 8): figures.Bishop, (7, 8): figures.Knight, (8, 8): figures.Rook,
 (1, 7): figures.Pawn, (2, 7): figures.Pawn, (3, 7): figures.Pawn, (4, 7): figures.Pawn, (5, 7): figures.Pawn, (6, 7): figures.Pawn, (7, 7): figures.Pawn, (8, 7): figures.Pawn,
 (1, 6): None, (2, 6): None, (3, 6): None, (4, 6): None, (5, 6): None, (6, 6): None, (7, 6): None, (8, 6): None,
 (1, 5): None, (2, 5): None, (3, 5): None, (4, 5): None, (5, 5): None, (6, 5): None, (7, 5): None, (8, 5): None,
 (1, 4): None, (2, 4): None, (3, 4): None, (4, 4): None, (5, 4): None, (6, 4): None, (7, 4): None, (8, 4): None,
 (1, 3): None, (2, 3): None, (3, 3): None, (4, 3): None, (5, 3): None, (6, 3): None, (7, 3): None, (8, 3): None,
 (1, 2): figures.Pawn, (2, 2): figures.Pawn, (3, 2): figures.Pawn, (4, 2): figures.Pawn, (5, 2): figures.Pawn, (6, 2): figures.Pawn, (7, 2): figures.Pawn, (8, 2): figures.Pawn,
 (1, 1): figures.Rook, (2, 1): figures.Knight, (3, 1): figures.Bishop, (4, 1): figures.Queen, (5, 1): figures.King, (6, 1): figures.Bishop, (7, 1): figures.Knight, (8, 1): figures.Rook,
}

BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
GREY = (128, 128, 128)

row = [i for i in range(1, 9)]
# column = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h']
# board = [[i + str(j) for i in column] for j in range(8, 0, -1)]
board = [[(i, j) for i in range(1, 9)] for j in range(8, 0, -1)]

black_gamer_cell_white_game = [board[i][j] for i in range(-2, 0) for j in range(0, 8)]
white_gamer_cell_white_game = [board[i][j] for i in range(0, 2) for j in range(0, 8)]
black_gamer_cell_black_game = [board[i][j] for i in range(0, 2) for j in range(0, 8)]
white_gamer_cell_black_game = [board[i][j] for i in range(-2, 0) for j in range(0, 8)]
wp = pygame.image.load(os.path.join(img_folder, 'wp.png'))
wk = pygame.image.load(os.path.join(img_folder, 'wk.png'))
wkn = pygame.image.load(os.path.join(img_folder, 'wkn.png'))
wb = pygame.image.load(os.path.join(img_folder, 'wb.png'))
wq = pygame.image.load(os.path.join(img_folder, 'wq.png'))
wr = pygame.image.load(os.path.join(img_folder, 'wr.png'))
bp = pygame.image.load(os.path.join(img_folder, 'bp.png'))
bk = pygame.image.load(os.path.join(img_folder, 'bk.png'))
bkn = pygame.image.load(os.path.join(img_folder, 'bkn.png'))
bb = pygame.image.load(os.path.join(img_folder, 'bb.png'))
bq = pygame.image.load(os.path.join(img_folder, 'bq.png'))
br = pygame.image.load(os.path.join(img_folder, 'br.png'))
wp.set_colorkey(BLACK)
wk.set_colorkey(BLACK)
wkn.set_colorkey(BLACK)
wb.set_colorkey(BLACK)
wq.set_colorkey(BLACK)
wr.set_colorkey(BLACK)
bp.set_colorkey(WHITE)
bk.set_colorkey(WHITE)
bkn.set_colorkey(WHITE)
bb.set_colorkey(WHITE)
bq.set_colorkey(WHITE)
br.set_colorkey(WHITE)


