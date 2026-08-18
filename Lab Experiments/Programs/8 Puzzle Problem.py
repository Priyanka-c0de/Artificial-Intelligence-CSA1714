import heapq
import copy

class State:
    def __init__(self, board, g=0, h=0, parent=None):
        self.board = board
        self.g = g  # Path cost
        self.h = h  # Heuristic cost
        self.f = g + h
        self.parent = parent

    def __lt__(self, other):
        return self.f < other.f

def get_blank_pos(board):
    for i in range(3):
        for j in range(3):
            if board[i][j] == 0:
                return i, j

def calculate_heuristic(board, goal):
    count = 0
    for i in range(3):
        for j in range(3):
            if board[i][j] != 0 and board[i][j] != goal[i][j]:
                count += 1
    return count

def get_neighbors(state, goal):
    neighbors = []
    x, y = get_blank_pos(state.board)
    moves = [(-1, 0), (1, 0), (0, -1), (0, 1)]  # Up, Down, Left, Right
    
    for dx, dy in moves:
        nx, ny = x + dx, y + dy
        if 0 <= nx < 3 and 0 <= ny < 3:
            new_board = copy.deepcopy(state.board)
            new_board[x][y], new_board[nx][ny] = new_board[nx][ny], new_board[x][y]
            
            g_new = state.g + 1
            h_new = calculate_heuristic(new_board, goal)
            neighbors.append(State(new_board, g_new, h_new, state))
            
    return neighbors

def print_board(board):
    for row in board:
        print(" ".join(map(str, row)))
    print()

def solve_8_puzzle(initial_board, goal_board):
    initial_h = calculate_heuristic(initial_board, goal_board)
    start_state = State(initial_board, 0, initial_h)
    
    open_list = []
    heapq.heappush(open_list, start_state)
    visited = set()
    
    while open_list:
        current_state = heapq.heappop(open_list)
        
        # Convert matrix to tuple to make it hashable for the visited set
        board_tuple = tuple(tuple(row) for row in current_state.board)
        
        if current_state.board == goal_board:
            path = []
            while current_state:
                path.append(current_state.board)
                current_state = current_state.parent
            return path[::-1]
            
        if board_tuple in visited:
            continue
        visited.add(board_tuple)
        
        for neighbor in get_neighbors(current_state, goal_board):
            neighbor_tuple = tuple(tuple(row) for row in neighbor.board)
            if neighbor_tuple not in visited:
                heapq.heappush(open_list, neighbor)
                
    return None

# Initial and Goal states
initial = [
    [1, 2, 3],
    [0, 4, 6],
    [7, 5, 8]
]

goal = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 0]
]

print("Initial State:")
print_board(initial)

solution_path = solve_8_puzzle(initial, goal)

if solution_path:
    print(f"Solution found in {len(solution_path) - 1} moves:\n")
    for step, board in enumerate(solution_path):
        print(f"Step {step}:")
        print_board(board)
else:
    print("No solution exists.")