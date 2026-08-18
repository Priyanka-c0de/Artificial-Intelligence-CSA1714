from collections import deque

def bfs(graph, start_node):
    visited = set()
    queue = deque([start_node])
    
    # Mark the start node as visited
    visited.add(start_node)
    
    print("BFS Traversal Order:", end=" ")
    
    while queue:
        # Dequeue a vertex from the front of the queue
        current_node = queue.popleft()
        print(current_node, end=" ")
        
        # Get all adjacent vertices of the dequeued vertex
        for neighbor in graph[current_node]:
            if neighbor not in visited:
                visited.add(neighbor)
                queue.append(neighbor)
    print()

# Graph represented as an adjacency list
graph = {
    'A': ['B', 'C'],
    'B': ['D', 'E'],
    'C': ['F'],
    'D': [],
    'E': ['F'],
    'F': []
}

# Run BFS starting from node 'A'
bfs(graph, 'A')