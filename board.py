import pprint
row = [i for i in range(1, 9)]
column = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h']
board = [[i + str(j) for i in column] for j in range(8, 0, -1)]
board_x_y = [[str(i) + str(j) for i in range(1, 9)] for j in range(8, 0, -1)]



