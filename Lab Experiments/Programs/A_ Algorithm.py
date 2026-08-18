import heapq

def a_star_algorithm(graph, heuristics, start, goal):
    # Priority Queue stores: (f_score, g_score, current_node, path)
    open_list = [(heuristics[start], 0, start, [start])]
    visited = set()

    while open_list:
        f, g, current, path = heapq.heappop(open_list)

        if current == goal:
            return path, g

        if current in visited:
            continue
        visited.add(current)

        for neighbor, weight in graph.get(current, []):
            if neighbor not in visited:
                new_g = g + weight
                new_f = new_g + heuristics[neighbor]
                heapq.heappush(open_list, (new_f, new_g, neighbor, path + [neighbor]))

    return None, float('inf')

# Adjacency list for graph representation
graph = {
    'A': [('B', 1), ('C', 3)],
    'B': [('D', 1), ('E', 5)],
    'C': [('F', 2)],
    'D': [('G', 3)],
    'E': [('G', 1)],
    'F': [('G', 1)],
    'G': []
}

# Heuristic value h(n) estimates distance to goal 'G'
heuristics = {
    'A': 6,
    'B': 4,
    'C': 4,
    'D': 2,
    'E': 1,
    'F': 1,
    'G': 0
}

start_node = 'A'
goal_node = 'G'

path, total_cost = a_star_algorithm(graph, heuristics, start_node, goal_node)

print(f"Shortest Path from {start_node} to {goal_node}: {' -> '.join(path)}")
print(f"Total Cost: {total_cost}")