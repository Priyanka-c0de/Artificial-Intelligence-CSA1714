def dfs(node, graph, visited=None):
    if visited is None:
        visited = set()
    
    # Mark the current node as visited and print it
    visited.add(node)
    print(node, end=" ")
    
    # Recur for all the vertices adjacent to this vertex
    for neighbor in graph[node]:
        if neighbor not in visited:
            dfs(neighbor, graph, visited)

# Graph represented as an adjacency list
graph = {
    'A': ['B', 'C'],
    'B': ['D', 'E'],
    'C': ['F'],
    'D': [],
    'E': ['F'],
    'F': []
}

print("DFS Traversal Order:", end=" ")
# Run DFS starting from node 'A'
dfs('A', graph)
print()