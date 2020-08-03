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
    if terminal(board):
        return False
    elif board is initial_state():
        return X
    else:
        flatten_board = []
        for sublist in board:
            for val in sublist:
                flatten_board.append(val)

        empty_count = flatten_board.count(EMPTY)

        if (empty_count % 2) == 0:
            return O
        elif (empty_count % 2) == 1:
            return X


def actions(board):
    """
    Returns set of all possible actions (i, j) available on the board.
    """
    possible_actions = set()

    for row, i in enumerate(board):
        for col, j in enumerate(i):
            if board[row][col] is EMPTY:
                possible_actions.add((row, col))

    return possible_actions


def result(board, action):
    """
    Returns the board that results from making move (i, j) on the board.
    """
    new_board = copy.deepcopy(board)
    (i, j) = action

    if board[i][j] is not EMPTY:
        raise Exception
    else:
        new_board[i][j] = player(board)
        return new_board


def winner(board):
    """
    Returns the winner of the game, if there is one.
    """
    for row in board:
        if row.count(row[0]) == len(row) and row[0] is not EMPTY:
            return row[0]

    for col in range(len(board)):
        vertical = []

        for row in board:
            vertical.append(row[col])

        if vertical.count(vertical[0]) == len(vertical) and vertical[0] is not EMPTY:
            return vertical[0]

    diagonal = []
    for index in range(len(board)):
        diagonal.append(board[index][index])

    if diagonal.count(diagonal[0]) == len(diagonal) and diagonal[0] is not EMPTY:
        return diagonal[0]

    reverse_diagonal = []
    for row, col in enumerate(reversed(range(len(board)))):
        reverse_diagonal.append(board[row][col])

    if reverse_diagonal.count(reverse_diagonal[0]) == len(reverse_diagonal) and reverse_diagonal[0] is not EMPTY:
        return reverse_diagonal[0]

    return None


def terminal(board):
    """
    Returns True if game is over, False otherwise.
    """
    if winner(board) is not None:
        return True
    elif not actions(board):
        return True
    else:
        return False


def utility(board):
    """
    Returns 1 if X has won the game, -1 if O has won, 0 otherwise.
    """
    if terminal(board):
        if winner(board) is X:
            return 1
        elif winner(board) is O:
            return -1
        else:
            return 0


def minimax(board):
    """
    Returns the optimal action for the current player on the board.
    """
    if terminal(board):
        return None

    if player(board) is X:
        best_score = -math.inf
        best_move = ()
        for action in actions(board):
            new_board = result(board, action)
            score = minimax_best_score(new_board)
            if score > best_score:
                best_score = score
                best_move = action

        return best_move

    else:
        best_score = math.inf
        best_move = ()
        for action in actions(board):
            new_board = result(board, action)
            score = minimax_best_score(new_board)
            if score < best_score:
                best_score = score
                best_move = action

        return best_move


def minimax_best_score(board):
    if terminal(board):
        return utility(board)

    if player(board) is X:
        v = -math.inf
        for action in actions(board):
            v = max(v, minimax_best_score(result(board, action)))
        return v

    else:
        v = math.inf
        for action in actions(board):
            v = min(v, minimax_best_score(result(board, action)))
        return v
