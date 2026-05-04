
def all_paths(graph, start, target):
    res = []
    path = []
    visited = set()

    def dfs(node):
        path.append(node)
        visited.add(node)

        if node == target:
            res.append(path.copy())
        else:
            for neighbor in graph.get(node, []):
                if neighbor not in visited:
                    dfs(neighbor)
        
        path.pop()
        visited.remove(node)
    
    dfs(start)
    return res


graph = {
    "A": ["B", "C"],
    "B": ["D"],
    "C": ["D"],
    "D": []
}

print(all_paths(graph, "A", "D"))