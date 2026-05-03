from collections import deque


def bfs_traversal(graph, start):
    queue = deque()
    visited = set()
    result = []

    queue.append(start)
    visited.add(start)

    while queue:
        current = queue.popleft()
        result.append(current)
        for neighbor in graph[current]:
            if neighbor not in visited:
                visited.add(neighbor)
                queue.append(neighbor)

    return result


graph = {
    'A': ['B', 'C'],
    'B': ['D'],
    'C': ['E'],
    'D': [],
    'E': []
}
start = 'A'

print(bfs_traversal(graph, start))