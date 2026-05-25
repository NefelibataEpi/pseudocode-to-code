"""
## Task: Dijkstra Path Reconstruction

### Write a function:
    def dijkstra_path(graph, start):

---

### New Requirement

Besides `dist`:
You must maintain:
    `parent = {}`

Meaning:
    `parent[v] = previous node on shortest path`

---

### During Relaxation

When updating shorter distance:
    `dist[neighbor] = new_dist`

also update:
    `parent[neighbor] = node`

---

### Return Rules

Return BOTH:
    `return dist, parent`

---

### Example

For graph:

```
graph = {
    0: [(1, 4), (2, 1)],
    1: [(3, 1)],
    2: [(1, 2), (3, 5)],
    3: []
}
```

Expected shortest path tree:

```
parent = {
    1: 2,
    2: 0,
    3: 1
}
```

Meaning:

`0 -> 2 -> 1 -> 3`
"""

import heapq

def dijkstra_path(graph, start):
    dist = {}
    parent = {}

    for node in graph:
        dist[node] = float("inf")

    dist[start] = 0

    heap = [(0, start)]

    while heap:
        current_dist, node = heapq.heappop(heap)

        if current_dist > dist[node]:
            continue

        for neighbor, weight in graph[node]:
            new_dist = current_dist + weight

            if new_dist < dist[neighbor]:
                dist[neighbor] = new_dist
                parent[neighbor] = node
                heapq.heappush(heap, (new_dist, neighbor))

    return dist, parent


def main():
    graph = {
        0: [(1, 4), (2, 1)],
        1: [(3, 1)],
        2: [(1, 2), (3, 5)],
        3: []
    }
    start = 0

    print(dijkstra_path(graph, start))


if __name__ == "__main__":
    main()