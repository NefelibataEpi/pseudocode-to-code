
def num_islands(grid):
    visited = set()
    num = 0
    
    for r in range(len(grid)):
        for c in range(len(grid[0])):
            if grid[r][c] == "1" and (r,c) not in visited:
                dfs(grid, (r,c), visited)
                num += 1
    
    return num


def dfs(grid, node, visited):
    visited.add(node)

    neighbors = get_neighbors(grid, node)
    for neighbor in neighbors:
        if neighbor not in visited:
            dfs(grid, neighbor, visited)



def get_neighbors(grid, node):
    rows, cols = len(grid), len(grid[0])
    r, c = node
    directions = [(-1,0), (1,0), (0,-1), (0, 1)]

    neighbors = []

    for dr, dc in directions:
        nr, nc = r+dr, c+dc
        if 0 <= nr < rows and 0 <= nc < cols:
            if grid[nr][nc] == "1":
                neighbors.append((nr, nc))
    
    return neighbors



grid = [
    ["1","1","0","0"],
    ["1","1","0","0"],
    ["0","0","1","0"],
    ["0","0","0","1"]
]

print(num_islands(grid))