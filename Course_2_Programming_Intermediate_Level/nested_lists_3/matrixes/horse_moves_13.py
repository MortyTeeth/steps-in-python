def init_board():
    board = []
    for i in range(8):
        line = []
        for k in range(8):
            line.append('.')
        board.append(line)
    return board


def assign_n(horse_coordinate):
    letter = horse_coordinate[0]
    number = horse_coordinate[1]
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h']
    numbers = ['8', '7', '6', '5', '4', '3', '2', '1']

    position_l = letters.index(letter)
    position_n = numbers.index(number)
    y = position_l
    x = position_n
    return x, y


def print_board(board):
    for n in range(8):
        print(*board[n])


def find_positions(board, x, y):
    if 0 <= x + 1 <= 7 and 0 <= y + 2 <= 7:
        board[x + 1][y + 2] = '*'
    if 0 <= x + 1 <= 7 and 0 <= y - 2 <= 7:
        board[x + 1][y - 2] = '*'
    if 0 <= x + 2 <= 7 and 0 <= y + 1 <= 7:
        board[x + 2][y + 1] = '*'
    if 0 <= x + 2 <= 7 and 0 <= y - 1 <= 7:
        board[x + 2][y - 1] = '*'
    if 0 <= x - 1 <= 7 and 0 <= y + 2 <= 7:
        board[x - 1][y + 2] = '*'
    if 0 <= x - 1 <= 7 and 0 <= y - 2 <= 7:
        board[x - 1][y - 2] = '*'
    if 0 <= x - 2 <= 7 and 0 <= y + 1 <= 7:
        board[x - 2][y + 1] = '*'
    if 0 <= x - 2 <= 7 and 0 <= y - 1 <= 7:
        board[x - 2][y - 1] = '*'
    return board


if True == True:
    board = init_board()
    x, y = assign_n(input())
    board[x][y] = 'N'

    print_board(find_positions(board, x, y))
