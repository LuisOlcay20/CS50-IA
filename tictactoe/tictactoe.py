"""
Tic Tac Toe Player
"""

import math
import copy

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
    #Contador Inicial
    x_moves = 0
    o_moves = 0

    #Recorremos todas las filas y celdas de la tabla de juego
    for row in board:
        for cell in row:
            if cell == "X":
                x_moves += 1
            if cell == "O":
                o_moves += 1
    
    #Decidimos a quien le toca jugar, considerando que el juego lo inicia X
    if x_moves > o_moves:
        return "O"
    else:
        return "X"
    
    raise NotImplementedError


def actions(board):
    """
    Returns set of all possible actions (i, j) available on the board.
    """
    possible_actions = set()

#Iteramos por el tablero, teniendo en cuenta posiciones y valores, guardamos posiciones EMPTY
    for i, row in enumerate(board):
        for j, cell in enumerate(row):
            if cell == None:
                possible_actions.add((i,j))

    return possible_actions
    raise NotImplementedError


def result(board, action):
    """
    Returns the board that results from making move (i, j) on the board.
    """
    updated_board = copy.deepcopy(board)
    i, j = action

    #Revisamos si el movimiento es posible
    if updated_board[i][j] is not None:
        raise Exception("Movement not allowed") 
    
    #Modificamos el tablero 
    current_player = player(board)
    updated_board[i][j] = current_player

    return updated_board
    raise NotImplementedError


def winner(board):
    """
    Returns the winner of the game, if there is one.
    """
    #Revisamos Filas
    for row in board:
        if row[0] ==  row[1] == row[2] and row[0] is not None:
            return row[0]
        
    #Revisamos Columnas
    for column in range(3):
        if board[0][column] == board[1][column] == board[2][column] and board[0][column] is not None:
            return board[0][column]
    
    #Revisamos Diagonales 
    if board[0][0] == board[1][1] == board[2][2] and board[0][0] is not None:
        return board[0][0]
    if board[0][2] == board[1][1] == board[2][0] and board[0][2] is not None:
        return board[0][2]
    
    return None
    raise NotImplementedError


def terminal(board):
    """
    Returns True if game is over, False otherwise.
    """
    #Existe Ganador
    if winner(board) is not None:
        return True
    
    #Revisemos que juego este completo y no exista ganador
    for row in board:
        for cell in row:
            if cell is None:
                return False
            
    return True
    raise NotImplementedError


def utility(board):
    """
    Returns 1 if X has won the game, -1 if O has won, 0 otherwise.
    """
    #traemos funcion winner
    win = winner(board)

    if win == "X":
        return 1
    elif win == "O":
        return -1
    else:
        return 0
    raise NotImplementedError

def minimax(board):
    """
    Returns the optimal action for the current player on the board.
    """
    #Si el juego esta terminado se retorna none
    if terminal(board):
        return None

    best_move = None
    current_player = player(board)

    if current_player == X:
        best_value = float("-inf")
        for action in actions(board):
            value = min_value(result(board, action))
            if value > best_value:
                best_value = value
                best_move = action
    else:
        best_value = float("inf")
        for action in actions(board):
            value = max_value(result(board, action))
            if value < best_value:
                best_value = value
                best_move = action

    return best_move

def max_value(board):
    if terminal(board):
        return utility(board)
    
    value = float("-inf")
    for action in actions(board):
        value = max(value, min_value(result(board, action)))
    return value

def min_value(board):
    if terminal(board):
        return utility(board)
    
    value = float("inf")
    for action in actions(board):
        value = min(value, max_value(result(board, action)))
    return value
