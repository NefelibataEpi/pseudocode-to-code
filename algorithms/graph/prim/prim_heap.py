"""
Task: Implement Prim's Algorithm with Min Heap

Write a function:
    def prim_heap(graph, start):

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
- Use a min heap to always get the current minimum-weight edge.
- Each heap element should be:
    (weight, from_vertex, to_vertex)
- Every time a new vertex is added, push all edges from that vertex to unvisited neighbors into the heap.
- Stop when all vertices are visited.

Return rules:
- Return a list of selected MST edges.
- Each selected edge should be:
    (from_vertex, to_vertex, weight)

Example:
Input:
start = "A"

Output:
[("A", "B", 2), ("B", "C", 1), ("B", "D", 4)]
"""

import heapq


def prim_heap(graph, start):
    visited = set([start])
    mst = []
    heap = []

    for neighbor, weight in graph[start]:
        heapq.heappush(heap, (weight, start, neighbor))

    while heap and len(visited) < len(graph):
        weight, from_vertex, to_vertex = heapq.heappop(heap)

        if to_vertex in visited:
            continue

        visited.add(to_vertex)
        mst.append((from_vertex, to_vertex, weight))

        for neighbor, w in graph[to_vertex]:
            if neighbor not in visited:
                heapq.heappush(heap, (w, to_vertex, neighbor))
    
    return mst


graph = {
    "A": [("B", 2), ("C", 3)],
    "B": [("A", 2), ("C", 1), ("D", 4)],
    "C": [("A", 3), ("B", 1), ("D", 5)],
    "D": [("B", 4), ("C", 5)]
}

start = "A"

# [("A", "B", 2), ("B", "C", 1), ("B", "D", 4)]
print(prim_heap(graph, start))