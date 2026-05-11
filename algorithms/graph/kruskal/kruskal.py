"""
## Task: Implement Kruskal's Algorithm

Write a function:

```python
def kruskal(n, edges):
```

Parameters:

- `n`: number of vertices
- `edges`: list of edges in format: (weight, u, v)

The function should:
- Return the edges in the Minimum Spanning Tree
- Use Union Find
- Sort edges by weight
- Avoid cycles

Return: `mst_edges`
where:

```python
mst_edges = [
    (weight, u, v),
    ...
]
```
"""

class UnionFind:
    def __init__(self, vertices):
        self.parent = []
        self.size = [1] * vertices

        for i in range(vertices):
            self.parent.append(i)

    def find(self, v):
        while v != self.parent[v]:
            v = self.parent[v]

        return v
    
    def union(self, p, q):
        pid = self.find(p)
        qid = self.find(q)

        p_size = self.size[pid]
        q_size = self.size[qid]

        if p_size < q_size:
            self.parent[pid] = qid
            self.size[qid] += self.size[pid]
        else:
            self.parent[qid] = pid
            self.size[pid] += self.size[qid]


    def connected(self, p, q):
        return self.find(p) == self.find(q)
    

def kruskal(n, edges):
    mst = []
    sorted_edges = sorted(edges)
    uf = UnionFind(n)

    for weight, u, v in sorted_edges:
        if len(mst) == n-1:
            break
        
        if not uf.connected(u, v):
            mst.append((weight, u, v))
            uf.union(u, v)
    
    return mst


def main():
    n = 4

    edges = [
        (1, 0, 1),
        (3, 0, 2),
        (2, 1, 2),
        (4, 2, 3)
    ]

    """
    [
        (1,0,1),
        (2,1,2),
        (4,2,3)
    ]  
    """
    print(kruskal(n, edges))


if __name__ == "__main__":
    main()