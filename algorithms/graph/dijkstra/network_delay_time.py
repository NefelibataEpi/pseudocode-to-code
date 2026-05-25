"""
## Task: Network Delay Time

### Problem

There are n nodes labeled from 1 to n.

You are given:

```
times = [
    [u, v, w]
]
```

Meaning: `u -> v takes w time`

---

### Goal

A signal starts from node k.

Return: **How long it takes for ALL nodes to receive the signal.**

If impossible: `return -1`

---

### Function
    `def network_delay_time(times, n, k):`

---

### Example 

Input:

```
times = [
    [2,1,1],
    [2,3,1],
    [3,4,1]
]
n = 4
k = 2
```

Output: `2`

---

Why?
2 -> 1 = 1
2 -> 3 = 1
2 -> 3 -> 4 = 2

The slowest node receives signal at time 2.
"""

import heapq

def network_delay_time(times, n, k):
    graph = {i: [] for i in range(1, n + 1)}

    for u, v, w in times:
        graph[u].append((v, w))
    
    dist = {i: float("inf") for i in range(1, n + 1)}

    dist[k] = 0

    heap = [(0, k)]

    while heap:
        current_dist, node = heapq.heappop(heap)

        if current_dist > dist[node]:
            continue

        for neighbor, weight in graph[node]:
            new_dist = current_dist + weight

            if new_dist < dist[neighbor]:
                dist[neighbor] = new_dist
                heapq.heappush(heap, (new_dist, neighbor))
    
    answer = max(dist.values())

    if answer == float("inf"):
        return -1
    
    return answer


def main():
    times = [
        [2,1,1],
        [2,3,1],
        [3,4,1]
    ]

    n = 4
    k = 2

    print(network_delay_time(times, n, k))


if __name__ == "__main__":
    main()