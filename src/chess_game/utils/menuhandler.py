from chess_game.utils.dataset import *
import pygame


class MenuHandler:
    def __init__(self):
        self.start_comp_game_bool = False
        self.start_game_friends_bool = False
        self.running = True
        self.menu_buttons = []
        self.menu_items = [
            (Text("Играть с компьютером", 20, BLACK), self.start_comp_game),
            (Text("Играть с другом", 20, BLACK), self.start_game_friends),
            (Text("Выход", 20, BLACK, bold=True), self.quit_game),
        ]

    def start_comp_game(self):
        self.start_comp_game_bool = True

    def start_game_friends(self):
        self.start_game_friends_bool = True

    def quit_game(self):
        self.running = False

    def create_menu_buttons(self, screen_width, screen_height):
        menu_buttons = []
        for i, (text, handler) in enumerate(self.menu_items):
            button = Button(
                x=screen_width // 2 - 250,
                y=100 + (100 + i) * i,
                w=500,
                h=100,
                text=text,
                on_click=handler,
            )
            menu_buttons.append(button)
        return menu_buttons

    def handle_events(self, screen_width, screen_height):
        self.menu_buttons = self.create_menu_buttons(screen_width, screen_height)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.running = False
            if event.type == pygame.MOUSEBUTTONUP:
                for b in self.menu_buttons:
                    # отслеживание нажатия кнопки и перехода к режиму игры
                    b.handle_mouse_up(pygame.mouse.get_pos())
        return self.menu_buttons

    def draw_menu(self, screen):
        screen.fill(BLACK)
        for b in self.menu_buttons:
            # отрисовка кнопок меню
            b.draw(screen)
