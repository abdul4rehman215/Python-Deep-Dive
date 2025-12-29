from collections import deque

# Graph represented as an adjacency list
graph = {
    'A': ['B', 'C'],
    'B': ['D', 'E'],
    'C': ['F'],
    'D': [],
    'E': ['F'],
    'F': []
}

# Breadth-First Search (BFS)
def bfs(start_node, graph):
    visited = set()
    queue = deque([start_node])

    while queue:
        node = queue.popleft()
        if node not in visited:
            print(node, end=" ")
            visited.add(node)
            queue.extend(
                neighbor for neighbor in graph[node]
                if neighbor not in visited
            )

# Depth-First Search (DFS)
def dfs(node, graph, visited=None):
    if visited is None:
        visited = set()

    if node not in visited:
        print(node, end=" ")
        visited.add(node)
        for neighbor in graph[node]:
            dfs(neighbor, graph, visited)

# Execute traversals
print("BFS Traversal:")
bfs('A', graph)
print("\nDFS Traversal:")
dfs('A', graph)
print()
