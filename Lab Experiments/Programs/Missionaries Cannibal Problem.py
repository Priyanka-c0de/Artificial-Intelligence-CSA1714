from collections import deque

def is_valid(m, c):
    # Check bounds
    if m < 0 or m > 3 or c < 0 or c > 3:
        return False
    # Check if cannibals outnumber missionaries on left bank
    if m > 0 and m < c:
        return False
    # Check if cannibals outnumber missionaries on right bank
    if (3 - m) > 0 and (3 - m) < (3 - c):
        return False
    return True

def solve_mc():
    # State format: (missionaries_left, cannibals_left, boat_left)
    initial_state = (3, 3, 1)
    goal_state = (0, 0, 0)
    
    # Queue stores tuple of (current_state, path_taken)
    queue = deque([(initial_state, [])])
    visited = set()
    
    # Possible boat combinations: (M, C)
    moves = [(1, 0), (2, 0), (0, 1), (0, 2), (1, 1)]
    
    while queue:
        curr_state, path = queue.popleft()
        m, c, b = curr_state
        
        if curr_state == goal_state:
            return path + [curr_state]
            
        if curr_state in visited:
            continue
        visited.add(curr_state)
        
        for dm, dc in moves:
            if b == 1:  # Boat moving Left -> Right
                next_state = (m - dm, c - dc, 0)
            else:       # Boat moving Right -> Left
                next_state = (m + dm, c + dc, 1)
                
            if is_valid(next_state[0], next_state[1]):
                if next_state not in visited:
                    queue.append((next_state, path + [curr_state]))
                    
    return None

def print_solution(path):
    for step, state in enumerate(path):
        m, c, b = state
        boat_side = "Left" if b == 1 else "Right"
        print(f"Step {step}: Left Bank [M:{m}, C:{c}] | Boat: {boat_side} | Right Bank [M:{3-m}, C:{3-c}]")

print("Solving Missionaries and Cannibals Problem:\n")
solution = solve_mc()

if solution:
    print_solution(solution)
else:
    print("No solution found.")