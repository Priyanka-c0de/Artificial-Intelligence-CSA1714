import itertools

def travelling_salesman_problem(graph, start):
    # Number of vertices
    n = len(graph)
    vertices = list(range(n))
    vertices.remove(start)
    
    min_path_weight = float('inf')
    best_path = []
    
    # Generate all possible permutations of remaining vertices
    for perm in itertools.permutations(vertices):
        current_path_weight = 0
        k = start
        
        # Calculate current path cost
        for next_city in perm:
            current_path_weight += graph[k][next_city]
            k = next_city
        
        # Add distance back to start city
        current_path_weight += graph[k][start]
        
        # Update minimum path
        if current_path_weight < min_path_weight:
            min_path_weight = current_path_weight
            best_path = [start] + list(perm) + [start]
            
    return min_path_weight, best_path

# Distance matrix representing weights between cities 0, 1, 2, 3
distance_matrix = [
    [0, 10, 15, 20],
    [10, 0, 35, 25],
    [15, 35, 0, 30],
    [20, 25, 30, 0]
]

start_vertex = 0
min_cost, optimal_route = travelling_salesman_problem(distance_matrix, start_vertex)

print(f"Optimal Path Cost: {min_cost}")
print(f"Optimal Path Route: {' -> '.join(map(str, optimal_route))}")