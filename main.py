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
            board_sprites_white.draw(screen_white_gamer)
            sprite_figures_white.draw(screen_white_gamer)
            board_sprites_black.draw(screen_black_gamer)
            sprite_figures_black.draw(screen_black_gamer)
            turn = 'white'
            count_turn = 0
            while game_run:
                clock.tick(FPS)
                # контроль ходов
                turn_bool = False
                screen.blit(screen_white_gamer, (0, 0))
                for event in pygame.event.get():
                    if event.type == pygame.QUIT:
                        game_run = False
                        start_game_friends_bool = False
                        running = False
                    if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                        # TODO!
                        pygame.mouse.get_rel()
                    if event.type == pygame.MOUSEBUTTONUP and event.button == 1:
                        turn_bool = True
                pos = pygame.mouse.get_pos()
                rect_cur = Cell('white', (1, 1))
                rect_cur.image = pygame.Surface((3, 3))
                rect_cur.rect = rect_cur.image.get_rect()
                rect_cur.rect.center = pos
                figure_focus = pygame.sprite.spritecollideany(rect_cur, sprite_figures_white)
                if figure_focus is not None and pygame.mouse.get_focused() and turn == figure_focus.color:
                    pressed = pygame.mouse.get_pressed()
                    if pressed[0]:
                        rel = pygame.mouse.get_rel()
                        figure_focus.rect.move_ip(rel)
                    board_sprites_white.draw(screen_white_gamer)
                    sprite_figures_white.draw(screen_white_gamer)
                    screen.fill(BLACK)
                    screen.blit(screen_white_gamer, (0, 0))
                    pygame.display.update()
                if turn_bool == True:
                    if turn == 'white':
                        turn = 'black'
                    elif turn == 'black':
                        turn = 'white'
                pygame.display.flip()

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


main()