"""
## Task: Implement Quick Union

Write a class:

```python
class QuickUnion:
```

The class should support:
- find(x)
- union(p, q)
- connected(p, q)

Rules:
- Use a parent array
- Each node initially points to itself
- `find(x)` should return the root of x
- `union(p, q)` should connect the roots
- `connected(p, q)` should check whether two nodes share the same root

Example:

```
uf = QuickUnion(5)

uf.union(0, 1)
uf.union(1, 2)

uf.connected(0, 2) -> True
uf.connected(0, 4) -> False
```
"""

class QuickUnion:
    def __init__(self, vertices):
        self.id = []
        for i in range(vertices):
            self.id.append(i)
    
    def find(self, v):
        while v != self.id[v]:
            v = self.id[v]
        
        return v
    
    def union(self, from_v, to_v):
        from_id = self.find(from_v)
        to_id = self.find(to_v)

        self.id[to_id] = from_id
    
    def connected(self, p, q):
        return self.find(p) == self.find(q)
    

def main():
    uf = QuickUnion(5)

    uf.union(0,1)
    uf.union(1,2)

    print(uf.connected(0,2)) # True
    print(uf.connected(0,4)) # False


if __name__ == "__main__":
    main()