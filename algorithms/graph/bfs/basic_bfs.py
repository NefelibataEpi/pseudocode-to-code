"""
Write a function:
    def bfs_traversal(graph, start):

Functionalities:
- `graph` is a dictionary (adjacency list)
- Start from node `start`
- Use a queue to traverse the graph in BFS order
- Do NOT use visited set yet

Return a list representing the visiting order

Example:
```
Input:
graph = {
    'A': ['B', 'C'],
    'B': ['D'],
    'C': ['E'],
    'D': [],
    'E': []
}
start = 'A'

Output:
['A', 'B', 'C', 'D', 'E']
```
"""

from collections import deque


def bfs_traversal(graph, start):
    queue = deque()
    visit = [start]

    queue.append(start)

    while queue:
        current = queue.popleft()
        for neighbor in graph[current]:
            if neighbor not in visit:
                visit.append(neighbor)
                queue.append(neighbor)

    return visit


graph = {
    'A': ['B', 'C'],
    'B': ['D'],
    'C': ['E'],
    'D': [],
    'E': []
}
start = 'A'

print(bfs_traversal(graph, start))