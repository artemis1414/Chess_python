import pygame
import chess_game.game.player as player
from chess_game.utils.dataset import *
from chess_game.game.board import Cell, board
from chess_game.utils.menuhandler import MenuHandler

start_comp_game_bool = False
start_game_friends_bool = False
running = True


def create_start_position_cell(
    cell, position, start_position, white_gamer_cell, black_gamer_cell
):
    if cell in white_gamer_cell:
        if start_position[cell] == figures.Pawn:
            position[cell] = start_position[cell]("white", wp.convert(), cell)
        elif start_position[cell] == figures.Rook:
            position[cell] = start_position[cell]("white", wr.convert(), cell)
        elif start_position[cell] == figures.Knight:
            position[cell] = start_position[cell]("white", wkn.convert(), cell)
        elif start_position[cell] == figures.Bishop:
            position[cell] = start_position[cell]("white", wb.convert(), cell)
        elif start_position[cell] == figures.Queen:
            position[cell] = start_position[cell]("white", wq.convert(), cell)
        elif start_position[cell] == figures.King:
            position[cell] = start_position[cell]("white", wk.convert(), cell)
    elif cell in black_gamer_cell:
        if start_position[cell] == figures.Pawn:
            position[cell] = start_position[cell]("black", bp.convert(), cell)
        elif start_position[cell] == figures.Rook:
            position[cell] = start_position[cell]("black", br.convert(), cell)
        elif start_position[cell] == figures.Knight:
            position[cell] = start_position[cell]("black", bkn.convert(), cell)
        elif start_position[cell] == figures.Bishop:
            position[cell] = start_position[cell]("black", bb.convert(), cell)
        elif start_position[cell] == figures.Queen:
            position[cell] = start_position[cell]("black", bq.convert(), cell)
        elif start_position[cell] == figures.King:
            position[cell] = start_position[cell]("black", bk.convert(), cell)
    else:
        position[cell] = None


def initialize_game():
    pygame.init()
    pygame.mixer.init()
    screen = pygame.display.set_mode((WIDTH, HEIGHT))
    pygame.display.set_caption("Шахматы")
    clock = pygame.time.Clock()
    return screen, clock


def main():
    menu_handler = MenuHandler()
    screen, clock = initialize_game()

    # Инициализация кнопок меню
    menu_buttons = menu_handler.create_menu_buttons(WIDTH, HEIGHT)
    running = True

    while running:
        clock.tick(FPS)
        if menu_handler.start_comp_game_bool:
            print("Игра с компьютером")
            # игра с компьютером
            break
        elif menu_handler.start_game_friends_bool:
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
                        board_cell = Cell(color="black", cell=cell)
                        create_start_position_cell(
                            cell,
                            position_white,
                            start_position_white,
                            white_gamer_cell_white_game,
                            black_gamer_cell_white_game,
                        )
                        board_sprites_white.add(board_cell)
                        if position_white[cell] is not None:
                            sprite_figures_white.add(position_white[cell])
                        board_cell = Cell(color="white", cell=cell)
                        create_start_position_cell(
                            cell,
                            position_black,
                            start_position_black,
                            white_gamer_cell_black_game,
                            black_gamer_cell_black_game,
                        )
                        board_sprites_black.add(board_cell)
                        if position_black[cell] is not None:
                            sprite_figures_black.add(position_black[cell])
                    else:
                        board_cell = Cell(color="white", cell=cell)
                        create_start_position_cell(
                            cell,
                            position_white,
                            start_position_white,
                            white_gamer_cell_white_game,
                            black_gamer_cell_white_game,
                        )
                        board_sprites_white.add(board_cell)
                        if position_white[cell] is not None:
                            sprite_figures_white.add(position_white[cell])
                        board_cell = Cell(color="black", cell=cell)
                        create_start_position_cell(
                            cell,
                            position_black,
                            start_position_black,
                            white_gamer_cell_black_game,
                            black_gamer_cell_black_game,
                        )
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
            turn = "white"
            count_turn = 0
            count_click = 0
            while game_run:
                clock.tick(FPS)
                # контроль ходов
                turn_bool = False
                take_figure = True
                screen.blit(screen_white_gamer, (0, 0))
                pos = pygame.mouse.get_pos()
                rect_cur = Cell("white", (1, 1))
                rect_cur.image = pygame.Surface((3, 3))
                rect_cur.rect = rect_cur.image.get_rect()
                rect_cur.rect.center = pos
                figure_focus = pygame.sprite.spritecollideany(
                    rect_cur, sprite_figures_white
                )
                for event in pygame.event.get():
                    if event.type == pygame.QUIT:
                        game_run = False
                        menu_handler.start_game_friends_bool = False
                        running = False
                    if event.type == pygame.MOUSEMOTION and count_click < 1:
                        take_figure = False
                    if event.type == pygame.MOUSEBUTTONDOWN:
                        if event.button == 1:
                            pygame.event.set_blocked(pygame.MOUSEBUTTONUP)
                            count_click += 1
                    if count_click == 2:
                        pygame.event.set_allowed(pygame.MOUSEBUTTONUP)
                        count_click = 0
                    if (
                        event.type == pygame.MOUSEBUTTONUP
                        and event.button == 1
                        and take_figure
                    ):
                        turn_bool = True
                if take_figure:
                    if (
                        figure_focus is not None
                        and pygame.mouse.get_focused()
                        and turn == figure_focus.color
                    ):
                        print(count_click, turn_bool)
                        pygame.mouse.get_rel()
                        figure_focus.rect.center = pos
                        board_sprites_white.draw(screen_white_gamer)
                        sprite_figures_white.draw(screen_white_gamer)
                        screen.fill(BLACK)
                        screen.blit(screen_white_gamer, (0, 0))
                board_sprites_white.draw(screen_white_gamer)
                sprite_figures_white.draw(screen_white_gamer)
                screen.fill(BLACK)
                screen.blit(screen_white_gamer, (0, 0))
                pygame.display.update()
                if turn_bool == True:
                    if turn == "white":
                        turn = "black"
                    elif turn == "black":
                        turn = "white"
                pygame.display.flip()
            break
        else:
            # Обработка событий меню и отрисовка кнопок
            menu_buttons = menu_handler.handle_events(WIDTH, HEIGHT)
            menu_handler.draw_menu(screen)
            pygame.display.flip()

    pygame.quit()


main()
