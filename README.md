# tic-tac-toe

This project uses the minmax algorithm to have an unbeatable tic-tac-toe bot.
To run, just run the Tic Tac Toe.py file


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
