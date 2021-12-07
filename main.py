import player
from board import board
import random


def main():
    print('Приветствуем в игре Шахматы!')
    name_player_1 = input('Введите имя первого игрока: ')
    name_player_2 = input('Введите имя второго игрока: ')
    x = input(f'''Выберите цвет:
    0 - {name_player_1} будет играть белыми,
    1 - {name_player_2} будет играть белыми,
    2 - случайно
    ''')
    while True:
        if x == '0':
            player_1 = player.Player('white', name_player_1)
            player_2 = player.Player('black', name_player_2)
            print(f'Отлично! {player_1} играет белыми, {player_2} играет черными!')
            break
        elif x == '1':
            player_1 = player.Player('black', name_player_1)
            player_2 = player.Player('white', name_player_2)
            print(f'Отлично! {player_2} играет белыми, {player_1} играет черными!')
            break
        else:
            x = random.choice(('0', '1'))


main()