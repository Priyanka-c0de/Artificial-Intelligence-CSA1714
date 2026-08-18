from collections import deque

def solve_water_jug(jug1_cap, jug2_cap, target):
    # Queue stores tuples of ((jug1, jug2), path_taken)
    queue = deque([((0, 0), [])])
    visited = set()

    while queue:
        (j1, j2), path = queue.popleft()

        # If target is achieved in either jug
        if j1 == target or j2 == target:
            return path + [(j1, j2)]

        if (j1, j2) in visited:
            continue
        visited.add((j1, j2))

        # Generate next possible rules/states
        next_states = [
            ((jug1_cap, j2), "Fill Jug 1"),
            ((j1, jug2_cap), "Fill Jug 2"),
            ((0, j2), "Empty Jug 1"),
            ((j1, 0), "Empty Jug 2"),
            # Pour Jug 1 -> Jug 2
            ((j1 - min(j1, jug2_cap - j2), j2 + min(j1, jug2_cap - j2)), "Pour Jug 1 into Jug 2"),
            # Pour Jug 2 -> Jug 1
            ((j1 + min(j2, jug1_cap - j1), j2 - min(j2, jug1_cap - j1)), "Pour Jug 2 into Jug 1")
        ]

        for state, action in next_states:
            if state not in visited:
                queue.append((state, path + [(j1, j2)]))

    return None

# Problem parameters
j1_capacity = 4
j2_capacity = 3
target_volume = 2

print(f"Solving Water Jug Problem for Capacities ({j1_capacity}, {j2_capacity}) and Target {target_volume}:\n")
solution = solve_water_jug(j1_capacity, j2_capacity, target_volume)

if solution:
    for step, state in enumerate(solution):
        print(f"Step {step}: Jug1 = {state[0]}L, Jug2 = {state[1]}L")
else:
    print("No solution possible.")