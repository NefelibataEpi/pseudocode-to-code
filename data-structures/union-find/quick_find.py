"""
## Task: Implement Quick Find

Write a class:

```python
class QuickFind:
```

The class should support:

- union(p, q)
- connected(p, q)

Rules:

- Each element initially belongs to its own group
- Use an array id
- If two elements belong to the same group,
- their id values should be equal

Example:

```
uf = QuickFind(5)

uf.union(0, 1)
uf.union(1, 2)

uf.connected(0, 2) -> True
uf.connected(0, 4) -> False
```
"""

class QuickFind:
    
    def __init__(self, vertices):
        self.graph = []
        for i in range(vertices):
            self.graph.append(i)

    def union(self, from_v, to_v):
        from_id = self.graph[from_v]
        to_id = self.graph[to_v]

        for i in range(len(self.graph)):
            if self.graph[i] == to_id:
                self.graph[i] = from_id
    
    def connected(self, from_v, to_v):
        return self.graph[from_v] == self.graph[to_v]


def main():
    uf = QuickFind(5)

    uf.union(0,1)
    uf.union(1,2)

    print(uf.connected(0,2)) # True
    print(uf.connected(0,4)) # False


if __name__ == "__main__":
    main()