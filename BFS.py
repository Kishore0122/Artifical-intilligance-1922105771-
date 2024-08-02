from collections import deque

def bfs(graph, start):
    visited = set()
    queue = deque([start])
    bfs_order = []

    while queue:
        vertex = queue.popleft()
        if vertex not in visited:
            visited.add(vertex)
            bfs_order.append(vertex)
            queue.extend(neighbor for neighbor in graph[vertex] if neighbor not in visited)

    return bfs_order

# Example usage
if __name__ == "__main__":
    graph = {
        'A': ['B', 'C'],
        'B': ['A', 'D', 'E'],
        'C': ['A', 'F'],
        'D': ['B'],
        'E': ['B', 'F'],
        'F': ['C', 'E']
    }

    start_vertex = 'A'
    bfs_result = bfs(graph, start_vertex)
    print("BFS Traversal Order:", bfs_result)
