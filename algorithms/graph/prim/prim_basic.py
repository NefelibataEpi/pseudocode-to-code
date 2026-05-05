"""
Task: Implement Basic Prim's Algorithm

Write a function:
    def prim_basic(graph, start):

The graph is represented as an adjacency list:

graph = {
    "A": [("B", 2), ("C", 3)],
    "B": [("A", 2), ("C", 1), ("D", 4)],
    "C": [("A", 3), ("B", 1), ("D", 5)],
    "D": [("B", 4), ("C", 5)]
}

Functionalities:
- Start from the given start vertex.
- Maintain a visited set.
- Repeatedly find the minimum-weight edge from visited vertices to unvisited vertices.
- Add that edge to the MST.
- Stop when all vertices are visited.

Return rules:
- Return a list of selected edges.
- Each edge should be represented as:
    (from_vertex, to_vertex, weight)

Example:
Input:
graph = {
    "A": [("B", 2), ("C", 3)],
    "B": [("A", 2), ("C", 1), ("D", 4)],
    "C": [("A", 3), ("B", 1), ("D", 5)],
    "D": [("B", 4), ("C", 5)]
}

start = "A"

Output:
[("A", "B", 2), ("B", "C", 1), ("B", "D", 4)]
"""

def prim_basic(graph, start):
    visited = set([start])
    path = []

    for _ in range(len(graph) - 1):
        min_edge = None
        min_weight = float('inf')

        for v in visited:
            for (neighbor, weight) in graph[v]:
                if neighbor not in visited:
                    if weight < min_weight:
                        min_weight = weight
                        min_edge = (v, neighbor, weight)
        
        path.append(min_edge)
        visited.add(min_edge[1])

    return path


graph = {
    "A": [("B", 2), ("C", 3)],
    "B": [("A", 2), ("C", 1), ("D", 4)],
    "C": [("A", 3), ("B", 1), ("D", 5)],
    "D": [("B", 4), ("C", 5)]
}

start = "A"

# [("A", "B", 2), ("B", "C", 1), ("B", "D", 4)]
print(prim_basic(graph, start))