"""
Task: Return Total Weight of MST (Prim)

Write a function:
    def prim_total_weight(graph, start):

Functionalities:
- Use your heap-based Prim algorithm
- Instead of returning edges, return the total weight of the MST

Return rules:
- Return an integer (sum of all selected edge weights)

Example:
Input:
start = "A"

Output:
7
"""

import heapq

def prim_total_weight(graph, start):
    total_weight = 0
    visited = set([start])
    heap = []

    for neighbor, weight in graph[start]:
        heapq.heappush(heap, (weight, start, neighbor))

    while heap and len(visited) < len(graph):
        weight, from_vertex, to_vertex = heapq.heappop(heap)

        if to_vertex in visited:
            continue

        visited.add(to_vertex)
        total_weight += weight

        for neighbor, w in graph[to_vertex]:
            if neighbor not in visited:
                heapq.heappush(heap, (w, to_vertex, neighbor))
    
    return total_weight


graph = {
    "A": [("B", 2), ("C", 3)],
    "B": [("A", 2), ("C", 1), ("D", 4)],
    "C": [("A", 3), ("B", 1), ("D", 5)],
    "D": [("B", 4), ("C", 5)]
}

start = "A"

print(prim_total_weight(graph, start)) # 7