import player
from dataset import *
from board import Cell, board
import random
import pygame


def main():
    position = {}
    def create_start_position_cell(cell, position):
        if cell in white_gamer_cell:
            if start_position[cell] == figures.Pawn:
                position[cell] = start_position[cell]('white', wp.convert(), cell)
            elif start_position[cell] == figures.Rook:
                position[cell] = start_position[cell]('white', wr.convert(), cell)
            elif start_position[cell] == figures.Knight:
                position[cell] = start_position[cell]('white', wkn.convert(), cell)
            elif start_position[cell] == figures.Bishop:
                position[cell] = start_position[cell]('white', wb.convert(), cell)
            elif start_position[cell] == figures.Queen:
                position[cell] = start_position[cell]('white', wq.convert(), cell)
            elif start_position[cell] == figures.King:
                position[cell] = start_position[cell]('white', wk.convert(), cell)
            sprite_figures.add(position[cell])
        elif cell in black_gamer_cell:
            if start_position[cell] == figures.Pawn:
                position[cell] = start_position[cell]('black', bp.convert(), cell)
            elif start_position[cell] == figures.Rook:
                position[cell] = start_position[cell]('black', bp.convert(), cell)
            elif start_position[cell] == figures.Knight:
                position[cell] = start_position[cell]('black', bkn.convert(), cell)
            elif start_position[cell] == figures.Bishop:
                position[cell] = start_position[cell]('black', bb.convert(), cell)
            elif start_position[cell] == figures.Queen:
                position[cell] = start_position[cell]('black', bq.convert(), cell)
            elif start_position[cell] == figures.King:
                position[cell] = start_position[cell]('black', bk.convert(), cell)
            sprite_figures.add(position[cell])
    pygame.init()
    pygame.mixer.init()
    screen = pygame.display.set_mode((WIDTH, HEIGHT))
    pygame.display.set_caption('Шахматы')
    clock = pygame.time.Clock()
    all_sprites = pygame.sprite.Group()
    sprite_figures = pygame.sprite.Group()
    count_color = 0
    for row in board:
        for cell in row:
            if count_color % 2 == 0:
                board_cell = Cell(color='white', cell=cell)
                create_start_position_cell(cell, position)
                print(board_cell.rect.center)
            else:
                board_cell = Cell(color='black', cell=cell)
                create_start_position_cell(cell, position)
            count_color += 1
            all_sprites.add(board_cell)
        count_color += 1
    running = True
    while running:
        clock.tick(FPS)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
        all_sprites.update()
        screen.fill(BLACK)
        all_sprites.draw(screen)
        sprite_figures.update()
        sprite_figures.draw(screen)
        pygame.display.flip()

    pygame.quit()
    # name_player_1 = input('Введите имя первого игрока: ')
    # name_player_2 = input('Введите имя второго игрока: ')
    # x = input(f'''Выберите цвет:
    # 0 - {name_player_1} будет играть белыми,
    # 1 - {name_player_2} будет играть белыми,
    # 2 - случайно
    # ''')
    # while True:
    #     if x == '0':
    #         player_1 = player.Player('white', name_player_1)
    #         player_2 = player.Player('black', name_player_2)
    #         print(f'Отлично! {player_1} играет белыми, {player_2} играет черными!')
    #         break
    #     elif x == '1':
    #         player_1 = player.Player('black', name_player_1)
    #         player_2 = player.Player('white', name_player_2)
    #         print(f'Отлично! {player_2} играет белыми, {player_1} играет черными!')
    #         break
    #     else:
    #         x = random.choice(('0', '1'))


main()