"""
Tic Tac Toe Player
"""

import math
from copy import deepcopy

X = "X"
O = "O"
EMPTY = None


def initial_state():
    """
    Returns starting state of the board.
    """
    return [[EMPTY, EMPTY, EMPTY],
            [EMPTY, EMPTY, EMPTY],
            [EMPTY, EMPTY, EMPTY]]

  

def player(board):
    """
    Returns player who has the next turn on a board.
    """
    Xcount = 0
    Ocount = 0

    for row in board:
        Xcount += row.count(X)
        Ocount += row.count(O)

    if Xcount <= Ocount:
        return X
    else:
        return O
    


def actions(board):
    """
    Returns set of all possible actions (i, j) available on the board.
    """
    possible_moves=set()
    for i , row in enumerate(board):
        for j,item in enumerate(row):
            if item==None:
                 possible_moves.add((i,j))
    
    return possible_moves 
     


def result(board, action):
    """
    Returns the board that results from making move (i, j) on the board.
    """
   


def winner(board):
    """
    Returns the winner of the game, if there is one.
    """
   
                               

def terminal(board):
    """
    Returns True if game is over, False otherwise.
    """
   
   

def utility(board):
    """
    Returns 1 if X has won the game, -1 if O has won, 0 otherwise.
    """



def minimax(board):
    """
    Returns the optimal action for the current player on the board.
    """

 
