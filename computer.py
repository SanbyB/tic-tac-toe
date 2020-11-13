import random
import play as pl


# random computer
def rand(board):
    free = []
    for i in range(len(board)):
        for j in range(len(board)):
            if board[i][j].state == '':  # checks for free square
                free.append((j, i))
    n = random.randint(0, len(free) - 1)  # chooses random free square
    return free[n]


# mimimax computer
def best_move(board, piece, turn, player):
    best_score = -20
    move = []
    for i in range(3):
        for j in range(3):
            if board[i][j].state == '':  # checks for free square
                pl.place(board, piece, (j, i))  # places a piece in square
                score = minimax(board, turn, player)  # calls the minimax function on the board
                pl.unplace(board, (j, i))  # and removes the placed piece
                if best_score < score:  # compares best (highest) result from minimax function
                    best_score = score
                    move.append((j, i))  # appends best position
    pl.place(board, piece, move[-1])


def minimax(board, turn, player):
    if player == 'minimax_comp':  # needed for if the AI plays first or second
        t = turn + 1
        p = 'X'
    else:
        t = turn
        p = 'O'

    if turn % 2 == 0:  # which pieces turn, alternates
        piece = 'X'
    else:
        piece = 'O'

    if pl.won(board):
        return (-1) ** t
    elif turn == 9:
        return 0
    else:  # if the board is still in play
        if piece == p:
            best_score = -20
            for i in range(3):
                for j in range(3):
                    if board[i][j].state == '':  # finds free square
                        pl.place(board, piece, (j, i))
                        score = minimax(board, turn + 1, player)  # calls iteration of function, increasing the turn which will change the piece
                        pl.unplace(board, (j, i))
                        best_score = max(score, best_score)  # maximized value returned for optimum play
            return best_score

        else:
            best_score = 20
            for i in range(3):
                for j in range(3):
                    if board[i][j].state == '':
                        pl.place(board, piece, (j, i))
                        score = minimax(board, turn + 1, player)
                        pl.unplace(board, (j, i))
                        best_score = min(score, best_score)  # minimized value returned for optimum play of opponent
            return best_score
