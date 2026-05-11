"""
## Task: Implement Weighted Quick Union

Write a class:

```python
class WeightedQuickUnion:
```

The class should support:
- `find(x)`
- `union(p, q)`
- `connected(p, q)`

Rules:
- Use:
    - parent array
    - size array
- Each node initially points to itself
- Each tree initially has size 1
- Always attach the smaller tree to the larger tree
- Update the size after union

Example:

```
uf = WeightedQuickUnion(5)

uf.union(0,1)
uf.union(1,2)

uf.connected(0,2) -> True
```
"""

class WeightedQuickUnion:
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
    

def main():
    uf = WeightedQuickUnion(5)

    uf.union(0,1)
    uf.union(1,2)

    print(uf.connected(0,2)) # True


if __name__ == "__main__":
    main()