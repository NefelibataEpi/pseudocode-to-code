"""
## Task: Kruskal with Total Weight and Connectivity Check

Write a function:

```python
def kruskal_with_weight(n, edges):
```

---

Functionalities:
- Use Kruskal's algorithm
- Return the MST edges
- Return the total weight of the MST
- If the graph is not connected, return None

---

Return Rules:
- If MST exists, return: `(mst_edges, total_weight)`
- If MST does not exist, return: `None`

---

Example:

```
n = 4
edges = [
    (1, 0, 1),
    (3, 0, 2),
    (2, 1, 2),
    (4, 2, 3)
]
```

Output: `([(1, 0, 1), (2, 1, 2), (4, 2, 3)], 7)`

---

Disconnected example:

```
n = 4
edges = [
    (1, 0, 1),
    (2, 2, 3)
]
```

Output: `None`
"""
import sys
import os

sys.path.append(
    os.path.abspath(
        os.path.join(os.path.dirname(__file__), "../../../")
    )
)

from data_structures.union_find.weighted_quick_union import WeightedQuickUnion

def kruskal_with_weight(n, edges):
    mst = []
    total_weight = 0

    sorted_edges = sorted(edges)
    uf = WeightedQuickUnion(n)

    for weight, u, v in sorted_edges:
        if not uf.connected(u, v):
            mst.append((weight, u, v))
            total_weight += weight
            uf.union(u, v)

        if len(mst) == n-1:
            return mst, total_weight
    
    return None


def main():
    n_1 = 4
    edges_1 = [
        (1, 0, 1),
        (3, 0, 2),
        (2, 1, 2),
        (4, 2, 3)
    ]

    # ([(1, 0, 1), (2, 1, 2), (4, 2, 3)], 7) 
    print(kruskal_with_weight(n_1, edges_1))

    n_2 = 4
    edges_2 = [
        (1, 0, 1),
        (2, 2, 3)
    ]

    # None
    print(kruskal_with_weight(n_2, edges_2))


if __name__ == "__main__":
    main()