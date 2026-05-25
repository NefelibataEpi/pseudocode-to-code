"""
## Task: Reconstruct Shortest Path

### Write a function:
    `def reconstruct_path(parent, start, target):`

---

### Functionalities

The function should rebuild the shortest path from start to target using the parent dictionary.

You should trace backwards:

`target -> parent[target] -> parent[parent[target]] -> ... -> start`

Then reverse the result.

---

### Return Rules
- If a path exists, return the path as a list.
- If target == start, return [start].
- If no path exists, return [].

---

### Example

Input:
```
parent = {
    1: 2,
    2: 0,
    3: 1
}
start = 0
target = 3
```

Output: `[0, 2, 1, 3]`
"""

def reconstruct_path(parent, start, target):
    if start == target:
        return [start]

    path = [target]
    current = target

    while current != start:

        if current not in parent:
            return []

        current = parent[current]
        path.append(current)

    path.reverse()

    return path


def main():
    parent = {
        1: 2,
        2: 0,
        3: 1
    }
    start = 0
    target = 3

    print(reconstruct_path(parent, start, target))


if __name__ == "__main__":
    main()