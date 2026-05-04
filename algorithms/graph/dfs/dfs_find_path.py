
def find_path(graph, start, target):
    visited = set()
    return dfs(graph, start, target, visited)


def dfs(graph, node, target, visited):
    if node == target:
        return [node]

    visited.add(node)

    for neighbor in graph.get(node, []):
        if neighbor not in visited:
            path = dfs(graph, neighbor, target, visited)
            if path:
                return [node] + path

    return None


graph = {
    "A": ["B", "C"],
    "B": ["A", "D"],
    "C": ["E"],
    "D": [],
    "E": []
}

print(find_path(graph, "A", "E"))