import graphics as gr


class Cell:
    def __init__(self, state):
        self.state = state


board = [[Cell('') for i in range(3)] for j in range(3)]


def position(click, width):
    '''
    Takes a pixel position clicked on the window
    and returns which square that corresponds to
    :param click:
    :return:
    '''
    square = []
    for c in click:
        square.append(c * 3 // width)
    return square


def place(board, piece, pos):
    '''
    Takes a piece and a position and places
    the piece on the board at the specified position
    :param piece:
    :param pos:
    :return:
    '''
    x = pos[0]
    y = pos[1]
    board[y][x].state = piece


def unplace(board, pos):
    '''
    Takes a piece and a position and places
    the piece on the board at the specified position
    :param piece:
    :param pos:
    :return:
    '''
    x = pos[0]
    y = pos[1]
    board[y][x].state = ''


def draw_board(board):  # draws the pieces on the board
    for i in range(len(board)):
        for j in range(len(board)):
            if board[i][j].state == 'X':
                gr.Piece((j, i)).draw_x()
            if board[i][j].state == 'O':
                gr.Piece((j, i)).draw_o()


def won(board):
    '''
    determines if a given board is won
    :param board:
    :return:
    '''
    n = 0
    for i in range(len(board)):
        if board[i][0].state == board[i][1].state == board[i][2].state != '':
            n += 1
        if board[0][i].state == board[1][i].state == board[2][i].state != '':
            n += 1
    if board[0][0].state == board[1][1].state == board[2][2].state != '':
        n += 1
    if board[0][2].state == board[1][1].state == board[2][0].state != '':
        n += 1
    if n != 0:
        return True
    else:
        return False
