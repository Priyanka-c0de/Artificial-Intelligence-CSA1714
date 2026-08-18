import math

def print_board(board):
    for row in board:
        print(" | ".join(row))
        print("-" * 9)

def check_winner(board, player):
    # Check rows, columns, and diagonals
    for i in range(3):
        if all(board[i][j] == player for j in range(3)) or \
           all(board[j][i] == player for j in range(3)):
            return True
    if all(board[i][i] == player for i in range(3)) or \
       all(board[i][2 - i] == player for i in range(3)):
        return True
    return False

def is_full(board):
    return all(cell != " " for row in board for cell in row)

def minimax(board, depth, is_maximizing):
    if check_winner(board, 'X'):
        return 10 - depth
    if check_winner(board, 'O'):
        return depth - 10
    if is_full(board):
        return 0

    if is_maximizing:
        best_score = -math.inf
        for r in range(3):
            for c in range(3):
                if board[r][c] == " ":
                    board[r][c] = 'X'
                    score = minimax(board, depth + 1, False)
                    board[r][c] = " "
                    best_score = max(score, best_score)
        return best_score
    else:
        best_score = math.inf
        for r in range(3):
            for c in range(3):
                if board[r][c] == " ":
                    board[r][c] = 'O'
                    score = minimax(board, depth + 1, True)
                    board[r][c] = " "
                    best_score = min(score, best_score)
        return best_score

def find_best_move(board):
    best_score = -math.inf
    best_move = None
    for r in range(3):
        for c in range(3):
            if board[r][c] == " ":
                board[r][c] = 'X'
                score = minimax(board, 0, False)
                board[r][c] = " "
                if score > best_score:
                    best_score = score
                    best_move = (r, c)
    return best_move

# Board initialization with an ongoing game state
board = [
    ['X', 'O', 'X'],
    ['O', 'O', ' '],
    [' ', 'X', ' ']
]

print("Current State of Board:")
print_board(board)

row, col = find_best_move(board)
board[row][col] = 'X'

print(f"AI ('X') chooses move at row {row}, column {col}:")
print_board(board)Tic