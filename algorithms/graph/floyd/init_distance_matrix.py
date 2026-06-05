"""
Task: Initialize Floyd Distance Matrix

Write a function:
    def init_distance_matrix(n, edges):

Functionalities:
- Create an n x n distance matrix.
- Initialize every value to float("inf").
- Set dist[i][i] = 0 for every vertex.
- For each edge (u, v, w), set dist[u][v] = w.
- Assume vertices are numbered from 0 to n - 1.

Return rules: Return the completed distance matrix.

Example:
```
n = 4
edges = [
    (0, 1, 3),
    (0, 2, 8),
    (1, 2, 2),
    (2, 3, 1)
]
```

Output:
```
[
    [0, 3, 8, inf],
    [inf, 0, 2, inf],
    [inf, inf, 0, 1],
    [inf, inf, inf, 0]
]
```
"""

def init_distance_matrix(n, edges):
    dist = [[float("inf") for _ in range(n)] for _ in range(n)]

    for i in range(n):
        dist[i][i] = 0
    
    for from_vertex, to_vertex, weight in edges:
        dist[from_vertex][to_vertex] = weight
    
    return dist


def main():
    n = 4
    edges = [
        (0, 1, 3),
        (0, 2, 8),
        (1, 2, 2),
        (2, 3, 1)
    ]
    print(init_distance_matrix(n, edges))


if __name__ == "__main__":
    main()