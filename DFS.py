def dfs_iterative(graph, start):
    visited = set()
    stack = [start]
    dfs_order = []

    while stack:
        vertex = stack.pop()
        if vertex not in visited:
            visited.add(vertex)
            dfs_order.append(vertex)
            stack.extend(neighbor for neighbor in reversed(graph[vertex]) if neighbor not in visited)

    return dfs_order

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
    dfs_result = dfs_iterative(graph, start_vertex)
    print("Iterative DFS Traversal Order:", dfs_result)
