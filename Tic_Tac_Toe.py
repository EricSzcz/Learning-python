
def display_board(board):
    for row in board:
        print(row)
    pass

def player_input():
    player1 = ''
    while player1 == '':
        player1 = input('Player1 chose your Symbol: X or O \n').upper()
        if (player1 != 'X') and (player1 != 'O'):
            player1 = ''
    if player1 == 'X':
        player2 = 'O'
        print('Sorry Player2 for you only left: ' + player2)
    else:
        player2 = 'X'
        print('Sorry Player2 for you only left: '+ player2)
    pass

def place_marker(board, marker, position):
    x = 0
    o = 0

    if marker == 'X':
        if position == '1':
            x += board[0][0]
            board [0][0] = 'X'
        elif position == '2':
            x += board[0][1]
            board [0][1] = 'X'
        elif position == '3':
            x += board[0][2]
            board [0][2] = 'X'
        elif position == '4':
            x += board[1][0]
            board [1][0] = 'X'
        elif position == '5':
            x += board[1][1]
            board[1][1] = 'X'
        elif position == '6':
            x += board[1][2]
            board [1][2] = 'X'
        elif position == '7':
            x += board[2][0]
            board [2][0] = 'X'
        elif position == '8':
            x += board[2][1]
            board [2][1] = 'X'
        elif position == '9':
            x += board[2][2]
            board [2][2] = 'X'
        else:
            print('num sei')

    if marker == 'O':
        if position == '1':
            o += board[0][0]
            board [0][0] = 'O'
        elif position == '2':
            o += board[0][1]
            board [0][1] = 'O'
        elif position == '3':
            o += board[0][2]
            board [0][2] = 'O'
        elif position == '4':
            o += board[1][0]
            board [1][0] = 'O'
        elif position == '5':
            o += board[1][1]
            board[1][1] = 'O'
        elif position == '6':
            o += board[1][2]
            board [1][2] = 'O'
        elif position == '7':
            o += board[2][0]
            board [2][0] = 'O'
        elif position == '8':
            o += board[2][1]
            board [2][1] = 'O'
        elif position == '9':
            o += board[2][2]
            board [2][2] = 'O'
        else:
            print('num sei')

        if x == 15:
            win_check('X')
        elif o == 15:
            win_check('O')
        else:
            win_check('Draw')

  #  positions = {'1': '[0][0]', '2': '[0][1]', '3': '[0][2]',
  #               '4': '[1][0]', '5': '[1][1]', '6': '[1][2]',
  #               '7': '[2][0]', '8': '[2][1]', '9': '[2][2]'}
    pass

def win_check(mark):
    if mark == 'Draw':
        print('Draw nobody won!')
    else:
        print(mark+' won!')
    pass

import random
def choose_first():
    if random.randint(1,2) == 1:
        return 'X'
    else:
        return 'O'

print('Welcome to Tic Tac Toe!')
l_1 = [2, 7, 6]
l_2 = [9, 5, 1]
l_3 = [4, 3, 8]
board = ([l_1, l_2, l_3])

display_board(board)
player_input()

first = choose_first()
if first == 'X':
    x = 1
    o = 0
else:
    x = 0
    o = 1

Lix = 0
while Lix < 9:
    if x == 1:
        print('X is your turn')
        position = input('write the number of the position where you wanna put your symbol')
        place_marker(board, first, position)
        x = 0
    else:
        print('O is your turn')
        position = input('write the number of the position where you wanna put your symbol')
        place_marker(board, first, position)
        x = 1
    Lix += Lix

