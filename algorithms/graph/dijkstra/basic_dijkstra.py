"""
## Task: Implement Basic Dijkstra Algorithm

### Write a function:
    def dijkstra(graph, start):

The function should find the shortest distance from start
to every other vertex in the graph using Dijkstra's Algorithm.

---

### Graph Format

The graph will use an adjacency list:

```
graph = {
    0: [(1, 4), (2, 1)],
    1: [(3, 1)],
    2: [(1, 2), (3, 5)],
    3: []
}
```

Meaning:

0 -> 1 weight 4
0 -> 2 weight 1

etc.

---

### Functionalities

You must:

- Use `heapq`
- Use a dist dictionary
- Initialize all distances to float("inf")
- Set: `dist[start] = 0`
- Use relaxation: `if current_dist + weight < dist[neighbor]:`

---

### Return Rules: Return the final dist dictionary.

### Example

Input:

```
graph = {
    0: [(1, 4), (2, 1)],
    1: [(3, 1)],
    2: [(1, 2), (3, 5)],
    3: []
}
start = 0
```

Expected output:

```
{
    0: 0,
    1: 3,
    2: 1,
    3: 4
}
```
"""

import heapq

def dijkstra(graph, start):
    dist = {}

    for node in graph:
        dist[node] = float("inf")

    dist[start] = 0

    heap = [(0, start)]

    while heap:
        current_dist, node = heapq.heappop(heap)

        if current_dist > dist[node]: continue

        for neighbor, weight in graph[node]:
            new_dist = current_dist + weight

            if new_dist < dist[neighbor]:
                dist[neighbor] = new_dist
                heapq.heappush(heap, (new_dist, neighbor))
    
    return dist

def main():
    graph = {
        0: [(1, 4), (2, 1)],
        1: [(3, 1)],
        2: [(1, 2), (3, 5)],
        3: []
    }

    start = 0

    print(dijkstra(graph, start))


if __name__ == "__main__":
    main()