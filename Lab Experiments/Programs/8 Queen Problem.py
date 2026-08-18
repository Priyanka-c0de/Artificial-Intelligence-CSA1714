def is_safe(board, row, col):
    # Check this row on left side
    for i in range(col):
        if board[row][i] == 1:
            return False

    # Check upper diagonal on left side
    for i, j in zip(range(row, -1, -1), range(col, -1, -1)):
        if board[i][j] == 1:
            return False

    # Check lower diagonal on left side
    for i, j in zip(range(row, 8, 1), range(col, -1, -1)):
        if board[i][j] == 1:
            return False

    return True

def solve_nq_util(board, col):
    # Base case: If all queens are placed
    if col >= 8:
        return True

    # Consider this column and try placing this queen in all rows one by one
    for i in range(8):
        if is_safe(board, i, col):
            board[i][col] = 1  # Place queen

            # Recur to place rest of the queens
            if solve_nq_util(board, col + 1):
                return True

            board[i][col] = 0  # Backtrack

    return False

def print_solution(board):
    for row in board:
        print(" ".join("Q" if x == 1 else "." for x in row))

# Initialize an empty 8x8 board
chess_board = [[0] * 8 for _ in range(8)]

if solve_nq_util(chess_board, 0):
    print("One valid configuration for 8-Queens:")
    print_solution(chess_board)
else:
    print("Solution does not exist")