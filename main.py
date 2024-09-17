import player
from dataset import *
from board import Cell, board
import random
import pygame

start_comp_game_bool = False
start_game_friends_bool = False
running = True

def main():
    global start_comp_game_bool
    global start_game_friends_bool
    global running

    def start_comp_game():
        global start_comp_game_bool
        start_comp_game_bool = True

    def start_game_friends():
        global start_game_friends_bool
        start_game_friends_bool = True

    def quit_game():
        global running
        running = False

    def create_start_position_cell(cell, position, start_position, white_gamer_cell, black_gamer_cell):
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
        elif cell in black_gamer_cell:
            if start_position[cell] == figures.Pawn:
                position[cell] = start_position[cell]('black', bp.convert(), cell)
            elif start_position[cell] == figures.Rook:
                position[cell] = start_position[cell]('black', br.convert(), cell)
            elif start_position[cell] == figures.Knight:
                position[cell] = start_position[cell]('black', bkn.convert(), cell)
            elif start_position[cell] == figures.Bishop:
                position[cell] = start_position[cell]('black', bb.convert(), cell)
            elif start_position[cell] == figures.Queen:
                position[cell] = start_position[cell]('black', bq.convert(), cell)
            elif start_position[cell] == figures.King:
                position[cell] = start_position[cell]('black', bk.convert(), cell)
        else:
            position[cell] = None

    menu = ((Text('Играть с компьютером', 20, BLACK), start_comp_game),
            (Text('Играть с другом', 20, BLACK), start_game_friends),
            (Text('Выход', 20, BLACK, bold=True), quit_game),
            # (Text('Продолжить сохраненную игру', 20, BLACK), continue_game),
            )
    # инициализация игры
    pygame.init()
    pygame.mixer.init()
    screen = pygame.display.set_mode((WIDTH, HEIGHT))
    pygame.display.set_caption('Шахматы')
    clock = pygame.time.Clock()
    menu_buttons = []
    while running:
        clock.tick(FPS)
        if start_comp_game_bool:
            # игра с компьютером
            continue
        elif start_game_friends_bool:
            # игра с другом
            # создание доски, фигур, расстановка позиции
            position_black = {}
            position_white = {}
            game_run = True
            board_sprites_white = pygame.sprite.Group()  # клетки для экрана белого
            sprite_figures_white = pygame.sprite.Group()  # фигуры экрана белого
            board_sprites_black = pygame.sprite.Group()  # клетки экрана черного
            sprite_figures_black = pygame.sprite.Group()  # фигуры экрана черного
            screen_white_gamer = pygame.Surface((WIDTH, HEIGHT))
            screen_black_gamer = pygame.Surface((WIDTH, HEIGHT))
            count_color = 0
            for row in board:
                for cell in row:
                    if count_color % 2 == 0:
                        board_cell = Cell(color='black', cell=cell)
                        create_start_position_cell(cell, position_white, start_position_white, white_gamer_cell_white_game,
                                                   black_gamer_cell_white_game)
                        board_sprites_white.add(board_cell)
                        if position_white[cell] is not None:
                            sprite_figures_white.add(position_white[cell])
                        board_cell = Cell(color='white', cell=cell)
                        create_start_position_cell(cell, position_black, start_position_black, white_gamer_cell_black_game,
                                                   black_gamer_cell_black_game)
                        board_sprites_black.add(board_cell)
                        if position_black[cell] is not None:
                            sprite_figures_black.add(position_black[cell])
                    else:
                        board_cell = Cell(color='white', cell=cell)
                        create_start_position_cell(cell, position_white, start_position_white, white_gamer_cell_white_game,
                                                   black_gamer_cell_white_game)
                        board_sprites_white.add(board_cell)
                        if position_white[cell] is not None:
                            sprite_figures_white.add(position_white[cell])
                        board_cell = Cell(color='black', cell=cell)
                        create_start_position_cell(cell, position_black, start_position_black, white_gamer_cell_black_game,
                                                   black_gamer_cell_black_game)
                        board_sprites_black.add(board_cell)
                        if position_black[cell] is not None:
                            sprite_figures_black.add(position_black[cell])
                    count_color += 1
                count_color += 1
            screen_white_gamer.fill(BLACK)
            screen_black_gamer.fill(BLACK)
            # Добавление всех элементов на экраны белого и черного
            for board_spr in board_sprites_white:
                screen_white_gamer.blit(board_spr.image, board_spr.rect)
            for figures_spr in sprite_figures_white:
                screen_white_gamer.blit(figures_spr.image, figures_spr.rect)
            for board_spr in board_sprites_black:
                screen_black_gamer.blit(board_spr.image, board_spr.rect)
            for figures_spr in sprite_figures_black:
                screen_black_gamer.blit(figures_spr.image, figures_spr.rect)
            turn = 'white'
            count_turn = 0
            while game_run:
                clock.tick(FPS)
                # контроль ходов
                if turn == 'white':
                    screen.blit(screen_white_gamer, (0, 0))
                elif turn == 'black':
                    screen.blit(screen_black_gamer, (0, 0))
                pygame.display.flip()
                for event in pygame.event.get():
                    if event.type == pygame.QUIT:
                        game_run = False
                        start_game_friends_bool = False
                        running = False
                    if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                        # первичный контроль ходов
                        turn = 'black'
                        count_turn += 1
                    elif event.type == pygame.MOUSEBUTTONDOWN and event.button == 3:
                        # первичный контроль ходов
                        turn = 'white'
                        count_turn += 1
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            if event.type == pygame.MOUSEBUTTONUP:
                for b in menu_buttons:
                    # отслеживание нажатия кнопки и перехода к режиму игры
                    b.handle_mouse_up(pygame.mouse.get_pos())
        for i, (text, handler) in enumerate(menu):
            # Инициализация кнопок меню
            button = Button(x=WIDTH // 2 - 250,
                            y=100 + (100 + i) * i,
                            w=500,
                            h=100,
                            text=text,
                            on_click=handler)
            menu_buttons.append(button)
        screen.fill(BLACK)
        for b in menu_buttons:
            # отрисовка кнопок
            b.draw(screen)
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