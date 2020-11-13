'''
Sets up tic tac toe using pygame as the interface,
the variables: 'rand_comp, minimax_comp, human' can be changed
to allow play between different types of player,
1 means the player will play and 0 means it won't,
the minimax AI does not work when playing against itself,
however all other possible combinations of player are possible.
The minimax AI, is implemented in the computer folder under the
definitions best_move and minimax, it uses an iterative process
to scan ahead assuming both players will play optimal moves,
and then returns a valid move so it will always win (/draw if the
opponent makes optimal moves too).
One flaw I have currently found is that the algorithm does not prioritise
moves until it wins, i.e. if it can win in 1 move but can force a win in 2 moves
either is chosen depending on which square is sooner on the scanning process.
This does not affect the end result but could be removed by implementing a higher
priority to finishing the game quicker.
The minimax alg closely follows the code from the Youtube tutorial:
Coding Challenge 154: Tic Tac Toe AI with Minimax Algorithm
published by: The Coding Train
'''

import pygame
import play as pl
import graphics as gr
import computer as cm

rand_comp = 0
minimax_comp = 1
human = 1
first_player = 'minimax_comp'

play_self = rand_comp + minimax_comp + human  # 2 humans can play each other, or 2 random computers

pygame.init()

running = True
playing = True
won = False
turn = 0

while running:
    for event in pygame.event.get():

        if event.type == pygame.QUIT:  # closes the game
            running = False

    while playing:
        if turn % 2 == 0:  # which pieces turn, alternates
            piece = 'X'
        else:
            piece = 'O'

        if human == 1:
            if (play_self != 1 and (first_player == 'human' and piece == 'X') or ( # sets up the human playing, weather it's playing
                    first_player != 'human' and piece == 'O')) or play_self == 1:  # another human, or a computer, and if it goes first or second
                for event in pygame.event.get():

                    if event.type == pygame.QUIT:  # closes the game, is repeated here so the game is still shown when it is finished being played
                        playing = False
                        running = False

                    click = pygame.mouse.get_pos()  # gets mouse position

                    if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:  # if left click
                        pos = pl.position(click, gr.width)  # gets coordinate square of where the piece is to be placed
                        x = pos[0]
                        y = pos[1]
                        if pl.board[y][x].state == '':  # if the square pressed is empty
                            pl.place(pl.board, piece, pos)  # place piece
                            turn += 1  # increase turn

        if rand_comp == 1:
            if (play_self != 1 and (first_player == 'rand_comp' and piece == 'X') or (  # same set up for computer as with the human
                    first_player != 'rand_comp' and piece == 'O')) or play_self == 1:
                r_pos = cm.rand(pl.board)  # random free board position
                pl.place(pl.board, piece, r_pos)
                turn += 1

        if minimax_comp == 1:
            if (play_self != 1 and (first_player == 'minimax_comp' and piece == 'X') or (
                    first_player != 'minimax_comp' and piece == 'O')) or play_self == 1:
                turn += 1
                cm.best_move(pl.board, piece, turn, first_player)  # finds the best move using minimax alg, called after the turn += 1
                                                                   # as that's how it is defined in the function see the line "elif turn == 9:"

        if pl.won(pl.board):
            playing = False  # stops play if a player has won
            won = True

        if turn == 9:
            playing = False  # stops play if all squares are full

        gr.draw_screen()  # draws the base
        pl.draw_board(pl.board)  # draws the pieces
        if won:
            gr.win(piece)  # draws win statement
        pygame.display.update()
