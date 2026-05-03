from collections import deque


def shortest_distance(grid, start, end):
    queue = deque([start])
    visited = set([start]) 
    distance = 0

    while queue:
        size = len(queue)

        for _ in range(size):
            current = queue.popleft()

            if current == end:
                return distance
        
            neighbors = get_neighbors(grid, current)
            for neighbor in neighbors:
                if neighbor not in visited:
                    visited.add(neighbor)
                    queue.append(neighbor)

        distance += 1

    return -1


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
print(shortest_distance(grid, start, end))