from collections import deque


def num_islands(grid):
    num = 0

    visited = set()

    for r in range(len(grid)):
        for c in range(len(grid[0])):
            if grid[r][c] == '1' and (r,c) not in visited:
                # init
                start = (r,c)
                queue = deque([start])
                visited.add(start)

                while queue:
                    current = queue.popleft()

                    neighbors = get_neighbors(grid, current)
                    for neighbor in neighbors:
                        if neighbor not in visited:
                            visited.add(neighbor)
                            queue.append(neighbor)
                
                num += 1

    return num


def get_neighbors(grid, current):
    rows, cols = len(grid), len(grid[0])
    r, c = current

    directions = [(-1,0), (1,0), (0, -1), (0, 1)]
    neighbors = []

    for dr, dc in directions:
        nr, nc = r + dr, c + dc

        if 0 <= nr < rows and 0 <= nc < cols:
            if grid[nr][nc] == '1':
                neighbors.append((nr, nc))
    
    return neighbors


grid = [
    ['1','1','0'],
    ['1','0','0'],
    ['0','0','1']
]

print(num_islands(grid))