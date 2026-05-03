from collections import deque

def shortest_path(grid, start, end):
    queue = deque([(start, [start])])
    visited = set([start])

    while queue:
        current, path = queue.popleft()

        if current == end:
            return path
        
        neighbors = get_neighbors(grid, current)
        for neighbor in neighbors:
            if neighbor not in visited:
                visited.add(neighbor)
                queue.append((neighbor, path + [neighbor]))
    
    return None


def get_neighbors(grid, current):
    rows, cols = len(grid), len(grid[0])
    r, c = current

    directions = [(-1,0), (1,0), (0, -1), (0, 1)]
    neighbors = []

    for dr, dc in directions:
        nr, nc = r + dr, c + dc

        if 0 <= nr < rows and 0 <= nc < cols:
            if grid[nr][nc] == 0:
                neighbors.append((nr, nc))
    
    return neighbors


grid = [
    [0, 0, 0],
    [1, 1, 0],
    [0, 0, 0]
]

start = (0, 0)
end = (2, 2)

# [(0,0), (0,1), (0,2), (1,2), (2,2)]
print(shortest_path(grid, start, end))